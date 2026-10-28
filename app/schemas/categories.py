from pydantic import BaseModel

class CategorySchema(BaseModel):
    id: str
    name: str

class CreateCategorySchema(BaseModel):
    name: str

class UpdateCategorySchema(BaseModel):
    name: str