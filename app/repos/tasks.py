from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models.tasks import TasksORM
from app.schemas.tasks import TaskCreateSchema


class TasksRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[TasksORM]:
        return self.db.scalars(select(TasksORM)).all()

    def get_by_id(self, task_id: str) -> TasksORM:
        return self.db.get(TasksORM, task_id)

    def create(self, task: TaskCreateSchema) -> TasksORM:
        new_task = TasksORM(title=task.title)
        self.db.add(new_task)
        return new_task

    def delete(self, task_orm):
        self.db.delete(task_orm)