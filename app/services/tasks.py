from sqlalchemy.orm import Session

from app.db.models.tasks import TasksORM
from app.repos.tasks import TasksRepository
from app.schemas.tasks import TaskCreateSchema, TaskUpdateSchema


class TasksService:
    def __init__(self, db: Session):
        self.db = db
        self.tasks_repo = TasksRepository(db)

    def list_tasks(self) -> list[TasksORM]:
        return self.tasks_repo.get_all()

    def create_task(self, task: TaskCreateSchema) -> TasksORM:
        return self.tasks_repo.create(task)

    def update_task(self, task_id: str, task: TaskUpdateSchema) -> TasksORM:
        task_for_update = self.tasks_repo.get_by_id(task_id)
        task_for_update.title = task.title if task.title else task_for_update.title
        task_for_update.completed = task.completed if task.completed is not None else task_for_update.completed
        self.db.commit()
        return task_for_update

    def delete_task(self, task_id: str):
        self.tasks_repo.delete(self.tasks_repo.get_by_id(task_id))