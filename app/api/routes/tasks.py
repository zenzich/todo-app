from fastapi import APIRouter, status, Depends, HTTPException

from app.api.dependencies import get_task_service
from app.core.exceptions import TaskNotFound
from app.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from app.services.tasks import TasksService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskSchema])
async def get_tasks(tasks_service: TasksService = Depends(get_task_service)) -> list[TaskSchema]:
    return await tasks_service.list_tasks()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskSchema)
async def create_task(payload: TaskCreateSchema, tasks_service: TasksService = Depends(get_task_service)) -> TaskSchema:
    return await tasks_service.create_task(payload)

@router.patch("/{task_id}", response_model=TaskUpdateSchema)
async def update_task(task_id: str, payload: TaskUpdateSchema, tasks_service: TasksService = Depends(get_task_service)) -> TaskSchema:
    try:
        return await tasks_service.update_task(task_id, payload)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str, tasks_service: TasksService = Depends(get_task_service)):
    try:
        return await tasks_service.delete_task(task_id)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)