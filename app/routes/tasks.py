import select
from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from uuid import uuid4
from app.db.session import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.tasks import TasksORM

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=TaskSchema)
def get_tasks(db: Session = Depends(get_db())) -> list[TaskSchema]:
    tasks_list = db.scalars(select(TasksORM)).all()
    return tasks_list

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateSchema, db: Session = Depends(get_db())) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4()), title=payload.title)
    tasks_list.append(new_task)
    return new_task

@router.patch("/{task_id}")
def update_task(task_id: str, payload: TaskUpdateSchema, db: Session = Depends(get_db())) -> TaskSchema:
    for task in tasks_list:
        if task.id == task_id:
            task.title = payload.title if payload.title else task.title
            task.completed = payload.completed if payload.completed is not None else task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, db: Session = Depends(get_db())):
    for task in tasks_list:
        if task.id == task_id:
            tasks_list.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")
