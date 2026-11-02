from fastapi import APIRouter, status, Depends, HTTPException

from app.api.dependencies import get_category_service
from app.core.exceptions import CategoryNotFound
from app.schemas.categories import CategorySchema, CreateCategorySchema, UpdateCategorySchema
from app.services.categories import CategoriesService

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[CategorySchema])
async def get_categories(categories_service: CategoriesService = Depends(get_category_service)) -> list[CategorySchema]:
    return await categories_service.list_categories()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategorySchema)
async def create_category(payload: CreateCategorySchema, categories_service: CategoriesService = Depends(get_category_service)) -> CategorySchema:
    return await categories_service.create_category(payload)

@router.patch("/{category_id}", response_model=UpdateCategorySchema)
async def update_category(category_id: str, payload: UpdateCategorySchema, categories_service: CategoriesService = Depends(get_category_service)) -> CategorySchema:
    try:
        return await categories_service.update_category(category_id, payload)
    except CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: str, categories_service: CategoriesService = Depends(get_category_service)):
    try:
        return await categories_service.delete_category(category_id)
    except CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)