import select
from fastapi import APIRouter, status, Depends

from app.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from app.db.session import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.tasks import TasksORM

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskSchema])
def get_tasks(db: Session = Depends(get_db)) -> list[TaskSchema]:
    tasks_list = db.scalars(select(TasksORM)).all()
    return tasks_list

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskSchema)
def create_task(payload: TaskCreateSchema, db: Session = Depends(get_db)) -> TaskSchema:
    new_task = TasksORM(title=payload.title)
    db.add(new_task)
    db.commit()
    return new_task

@router.patch("/{task_id}", response_model=TaskUpdateSchema)
def update_task(task_id: str, payload: TaskUpdateSchema, db: Session = Depends(get_db)) -> TaskSchema:
    task_for_update = db.get(TasksORM, task_id)
    task_for_update.title = payload.title if payload.title else task_for_update.title
    task_for_update.completed = payload.completed if payload.completed is not None else task_for_update.completed
    db.commit()

    return task_for_update

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, db: Session = Depends(get_db)):
    task_for_delete = db.get(TasksORM, task_id)
    db.delete(task_for_delete)
    db.commit()
