from fastapi import APIRouter, HTTPException, status
from app.schemas.categories import CategorySchema, CreateCategorySchema, UpdateCategorySchema
from uuid import uuid4

router = APIRouter(prefix="/categories", tags=["Categories"])

categories_list: list[CategorySchema] = []

@router.get("/")
def get_categories() -> list[CategorySchema]:
    return categories_list

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_category(category: CreateCategorySchema) -> CategorySchema:
    new_category = CategorySchema(id = str(uuid4()), name = category.name)
    categories_list.append(new_category)
    return new_category

@router.patch("/{category_id}")
def update_category(category_id: str, updated_category: UpdateCategorySchema) -> CategorySchema:
    for category in categories_list:
        if category.id == category_id:
            category.name = updated_category.name
            return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str):
    for category in categories_list:
        if category.id == category_id:
            categories_list.remove(category)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)