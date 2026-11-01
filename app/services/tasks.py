from sqlalchemy.orm import Session

from app.core.exceptions import TaskNotFound
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
        new_task = self.tasks_repo.create(task)
        self.db.commit()
        return new_task

    def update_task(self, task_id: str, task: TaskUpdateSchema) -> TasksORM:
        try:
            task_for_update = self.tasks_repo.get_by_id(task_id)
        except Exception:
            raise TaskNotFound(f"Task not found id:{task_id}")
        task_for_update.title = task.title if task.title else task_for_update.title
        task_for_update.completed = task.completed if task.completed is not None else task_for_update.completed
        self.db.commit()
        return task_for_update

    def delete_task(self, task_id: str):
        try:
            task_for_delete = self.tasks_repo.get_by_id(task_id)
        except Exception:
            raise TaskNotFound(f"Task not found id:{task_id}")
        self.tasks_repo.delete(task_for_delete)
        self.db.commit()