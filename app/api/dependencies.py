from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.tasks import TasksService

def get_task_service(db: Session = Depends(get_db)):
    return TasksService(db)