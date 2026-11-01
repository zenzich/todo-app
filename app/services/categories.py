from sqlalchemy.orm import Session

from app.db.models.categories import CategoriesORM
from app.repos.categories import CategoryRepository
from app.schemas.categories import CreateCategorySchema, UpdateCategorySchema


class CategoriesService:
    def __init__(self, db: Session):
        self.db = db
        self.categories_repo = CategoryRepository(db)

    def list_categories(self) -> list[CategoriesORM]:
        return self.categories_repo.get_all()

    def create_category(self, category: CreateCategorySchema) -> CategoriesORM:
        return self.categories_repo.create(category)

    def update_category(self, category_id: str, category: UpdateCategorySchema) -> CategoriesORM:
        category_for_update = self.categories_repo.get_by_id(category_id)
        category_for_update.name = category.name if category.name else category_for_update.name
        self.db.commit()
        return category_for_update

    def delete_category(self, category_id: str):
        self.categories_repo.delete(self.categories_repo.get_by_id(category_id))