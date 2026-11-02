from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import TaskNotFound
from app.db.models.tasks import TasksORM
from app.repos.tasks import TasksRepository
from app.schemas.tasks import TaskCreateSchema, TaskUpdateSchema


class TasksService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.tasks_repo = TasksRepository(db)

    async def list_tasks(self) -> list[TasksORM]:
        return await self.tasks_repo.get_all()

    async def create_task(self, task: TaskCreateSchema) -> TasksORM:
        new_task = await self.tasks_repo.create(task)
        await self.db.commit()
        return new_task

    async def update_task(self, task_id: str, task: TaskUpdateSchema) -> TasksORM:
        task_for_update = await self.tasks_repo.get_by_id(task_id)
        if not task_for_update:
            raise TaskNotFound(f"Task not found id:{task_id}")
        task_for_update.title = task.title if task.title else task_for_update.title
        task_for_update.completed = task.completed if task.completed is not None else task_for_update.completed
        await self.db.commit()
        return task_for_update

    async def delete_task(self, task_id: str):
        task_for_delete = await self.tasks_repo.get_by_id(task_id)
        if not task_for_delete:
            raise TaskNotFound(f"Task not found id:{task_id}")
        await self.tasks_repo.delete(task_for_delete)
        await self.db.commit()