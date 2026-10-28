from fastapi import APIRouter, HTTPException
from app.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from uuid import uuid4

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_list: list[TaskSchema] = []

@router.get("/")
def get_tasks() -> list[TaskSchema]:
    return tasks_list

@router.post("/")
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4()), title=payload.title)
    tasks_list.append(new_task)
    return new_task

@router.patch("/{task_id}")
def update_task(task_id: str, payload: TaskUpdateSchema) -> TaskSchema:
    for task in tasks_list:
        if task.id == task_id:
            task.title = payload.title if payload.title else task.title
            task.completed = payload.completed if payload.completed is not None else task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")
