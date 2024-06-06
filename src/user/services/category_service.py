from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService
from ..repositories.category_repository import category_repository


class CategoryService(BaseService):

    async def get_all(self) -> list[ModelType] | None:
        return await self.repository.all()

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


category_service = CategoryService(repository=category_repository)
