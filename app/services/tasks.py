from sqlalchemy.ext.asyncio import AsyncSession

from app.cache.redis_model import RedisCache
from app.core.exceptions import TaskNotFound
from app.db.models.tasks import TasksORM
from app.repos.tasks import TasksRepository
from app.schemas.tasks import TaskCreateSchema, TaskUpdateSchema, TaskSchema
from app.core.config import settings

class TasksService:
    def __init__(self, db: AsyncSession, cache_url: str = settings.REDIS_URL, cache_ttl_seconds: int = settings.CACHE_TTL_SECONDS, cache_tasks_key: str = settings.CACHE_TASKS_KEY):
        self.db = db
        self.tasks_repo = TasksRepository(db)
        self.cache = RedisCache(cache_url, cache_ttl_seconds)
        self.cache_key = cache_tasks_key

    async def list_tasks(self) -> list[TasksORM]:
        cached_tasks = await self.cache.get(self.cache_key)
        if cached_tasks: return cached_tasks

        tasks = await self.tasks_repo.get_all()
        tasks_for_cache = [TaskSchema.model_validate(task).model_dump() for task in tasks]
        await self.cache.set(self.cache_key, tasks_for_cache)

        return tasks

    async def create_task(self, task: TaskCreateSchema) -> TasksORM:
        await self.cache.delete(self.cache_key)

        new_task = await self.tasks_repo.create(task)
        await self.db.commit()
        return new_task

    async def update_task(self, task_id: str, task: TaskUpdateSchema) -> TasksORM:
        await self.cache.delete(self.cache_key)

        task_for_update = await self.tasks_repo.get_by_id(task_id)
        if not task_for_update:
            raise TaskNotFound(f"Task not found id:{task_id}")
        task_for_update.title = task.title if task.title else task_for_update.title
        task_for_update.completed = task.completed if task.completed is not None else task_for_update.completed
        await self.db.commit()
        return task_for_update

    async def delete_task(self, task_id: str):
        await self.cache.delete(self.cache_key)

        task_for_delete = await self.tasks_repo.get_by_id(task_id)
        if not task_for_delete:
            raise TaskNotFound(f"Task not found id:{task_id}")
        await self.tasks_repo.delete(task_for_delete)
        await self.db.commit()