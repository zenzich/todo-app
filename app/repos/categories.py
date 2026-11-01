from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models.categories import CategoriesORM
from app.schemas.categories import CreateCategorySchema


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[CategoriesORM]:
        return self.db.scalars(select(CategoriesORM)).all()

    def get_by_id(self, category_id: str) -> CategoriesORM:
        return self.db.get(CategoriesORM, category_id)

    def create(self, category: CreateCategorySchema) -> CategoriesORM:
        new_category = CategoriesORM(name=category.name)
        self.db.add(new_category)
        self.db.commit()
        return new_category

    def delete(self, category_orm):
        self.db.delete(category_orm)
        self.db.commit()