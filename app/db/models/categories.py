from app.db.base_class import Base
from sqlalchemy.orm import Mapped

class CategoriesORM(Base):
    __tablename__ = "categories"

    name: Mapped[str]