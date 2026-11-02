from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.tasks import TasksORM
from app.schemas.tasks import TaskCreateSchema


class TasksRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[TasksORM]:
        tasks = await self.db.scalars(select(TasksORM))
        return tasks.all()

    async def get_by_id(self, task_id: str) -> TasksORM | None:
        return await self.db.get(TasksORM, task_id)

    async def create(self, task: TaskCreateSchema) -> TasksORM:
        new_task = TasksORM(title=task.title)
        self.db.add(new_task)
        return new_task

    async def delete(self, task_orm):
        await self.db.delete(task_orm)