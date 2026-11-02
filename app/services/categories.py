from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import CategoryNotFound
from app.db.models.categories import CategoriesORM
from app.repos.categories import CategoryRepository
from app.schemas.categories import CreateCategorySchema, UpdateCategorySchema


class CategoriesService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.categories_repo = CategoryRepository(db)

    async def list_categories(self) -> list[CategoriesORM]:
        return await self.categories_repo.get_all()

    async def create_category(self, category: CreateCategorySchema) -> CategoriesORM:
        new_category = await self.categories_repo.create(category)
        await self.db.commit()
        return new_category

    async def update_category(self, category_id: str, category: UpdateCategorySchema) -> CategoriesORM:
        category_for_update = await self.categories_repo.get_by_id(category_id)
        if not category_for_update:
            raise CategoryNotFound(f"Category not found id:{category_id}")
        category_for_update.name = category.name if category.name else category_for_update.name
        await self.db.commit()
        return category_for_update

    async def delete_category(self, category_id: str):
        category_to_delete = await self.categories_repo.get_by_id(category_id)
        if not category_to_delete:
            raise CategoryNotFound(f"Category not found id:{category_id}")
        await self.categories_repo.delete(category_to_delete)
        await self.db.commit()