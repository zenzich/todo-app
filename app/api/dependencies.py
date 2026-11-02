from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.tasks import TasksService
from app.services.categories import CategoriesService

async def get_task_service(db: AsyncSession = Depends(get_db)):
    return TasksService(db)

async def get_category_service(db: AsyncSession = Depends(get_db)):
    return CategoriesService(db)