from fastapi import APIRouter, status, Depends

from app.api.dependencies import get_category_service
from app.schemas.categories import CategorySchema, CreateCategorySchema, UpdateCategorySchema
from app.services.categories import CategoriesService

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[CategorySchema])
def get_categories(categories_service: CategoriesService = Depends(get_category_service)) -> list[CategorySchema]:
    return categories_service.list_categories()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategorySchema)
def create_category(payload: CreateCategorySchema, categories_service: CategoriesService = Depends(get_category_service)) -> CategorySchema:
    return categories_service.create_category(payload)

@router.patch("/{category_id}", response_model=UpdateCategorySchema)
def update_category(category_id: str, payload: UpdateCategorySchema, categories_service: CategoriesService = Depends(get_category_service)) -> CategorySchema:
    return categories_service.update_category(category_id, payload)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str, categories_service: CategoriesService = Depends(get_category_service)):
    return categories_service.delete_category(category_id)