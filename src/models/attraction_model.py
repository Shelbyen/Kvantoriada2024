from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class AttractionModel(Base):
    __tablename__ = "attractions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    town_id: Mapped[int] = mapped_column(ForeignKey("towns.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")
    address: Mapped[str] = mapped_column(String, default="Moscow")
    main_photo: Mapped[str] = mapped_column(String)
    another_photo: Mapped[str] = mapped_column(String)
