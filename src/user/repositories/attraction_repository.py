from sqlalchemy import select
from sqlalchemy.orm import load_only

from src.repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from src.models.attraction_model import AttractionModel
from src.config.database.db_helper import db_helper

from ..schemas.attraction_schema import AttractionCreate, AttractionUpdate


class AttractionRepository(SqlAlchemyRepository[ModelType, AttractionCreate, AttractionUpdate]):
    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int = 100,
            offset: int = 0,
    ) -> list[ModelType] | None:
        async with self._session_factory() as session:
            stmt = select(self.model)
            if fields:
                model_fields = [getattr(self.model, field) for field in fields]
                stmt = stmt.options(load_only(*model_fields))
            if order:
                stmt = stmt.order_by(*order)
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            rows = await session.execute(stmt)
            return list(rows.scalars().all())

    async def filter_parameters(
            self,
            town_ids: list[int] | None = None,
            category_ids: list[int] | None = None
    ) -> list[ModelType] | None:
        async with self._session_factory() as session:
            stmt = select(self.model)
            if town_ids:
                stmt = stmt.where(self.model.town_id.in_(town_ids))
            if category_ids:
                stmt = stmt.where(self.model.category_id.in_(category_ids))
            rows = await session.execute(stmt)
            return list(rows.scalars().all())

    async def all(self) -> list[ModelType] | None:
        return await self.filter()

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        async with self._session_factory() as session:
            result = await session.execute(stmt)
            return result.scalar() is not None


attraction_repository = AttractionRepository(model=AttractionModel, db_session=db_helper.get_db_session)
