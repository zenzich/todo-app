from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.categories import CategoriesORM
from app.schemas.categories import CreateCategorySchema


class CategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[CategoriesORM]:
        categories = await self.db.scalars(select(CategoriesORM))
        return categories.all()

    async def get_by_id(self, category_id: str) -> CategoriesORM | None:
        return await self.db.get(CategoriesORM, category_id)

    async def create(self, category: CreateCategorySchema) -> CategoriesORM:
        new_category = CategoriesORM(name=category.name)
        self.db.add(new_category)
        return new_category

    async def delete(self, category_orm):
        await self.db.delete(category_orm)