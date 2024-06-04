from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class TownModel(Base):
    __tablename__ = "towns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
