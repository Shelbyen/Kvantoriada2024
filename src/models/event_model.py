from datetime import datetime

from sqlalchemy import String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class EventModel(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    town_id: Mapped[int] = mapped_column(ForeignKey("towns.id"))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")
    address: Mapped[str] = mapped_column(String, default="Moscow")
    start: Mapped[datetime] = mapped_column(DateTime)
    end: Mapped[datetime] = mapped_column(DateTime)
    main_photo: Mapped[str] = mapped_column(String)
    another_photo: Mapped[str] = mapped_column(String)

