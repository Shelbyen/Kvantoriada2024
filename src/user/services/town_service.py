from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService
from ..repositories.town_repository import town_repository


class TownService(BaseService):

    async def get_all(self) -> list[ModelType] | None:
        return await self.repository.all()

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


town_service = TownService(repository=town_repository)
