from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService
from ..repositories.attraction_repository import attraction_repository


class AttractionService(BaseService):

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[ModelType] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def filter_with_replacement(
            self,
            town_ids: list[int] | None = None,
            category_ids: list[int] | None = None
    ) -> list[ModelType] | None:
        return await self.repository.filter_parameters(
            town_ids=town_ids,
            category_ids=category_ids
        )

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


attraction_service = AttractionService(repository=attraction_repository)
