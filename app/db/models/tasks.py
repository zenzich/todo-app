from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column

class TasksORM(Base):
    __tablename__ = "tasks"

    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)