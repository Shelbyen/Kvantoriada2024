from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    pass


class CategoryUpdate(BaseModel):
    pass


class CategoryResponse(BaseModel):
    id: int


class CategoryListResponse(BaseModel):
    id: int | None = None
    name: str | None = None
