from fastapi import APIRouter, status, Depends

from app.api.dependencies import get_task_service
from app.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from app.services.tasks import TasksService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskSchema])
def get_tasks(tasks_service: TasksService = Depends(get_task_service)) -> list[TaskSchema]:
    return tasks_service.list_tasks()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskSchema)
def create_task(payload: TaskCreateSchema, tasks_service: TasksService = Depends(get_task_service)) -> TaskSchema:
    return tasks_service.create_task(payload)

@router.patch("/{task_id}", response_model=TaskUpdateSchema)
def update_task(task_id: str, payload: TaskUpdateSchema, tasks_service: TasksService = Depends(get_task_service)) -> TaskSchema:
    return tasks_service.update_task(task_id, payload)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, tasks_service: TasksService = Depends(get_task_service)):
    return tasks_service.delete_task(task_id)