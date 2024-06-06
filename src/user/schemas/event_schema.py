from typing import Union
from datetime import datetime

from pydantic import BaseModel


class EventBase(BaseModel):
    id: int
    town_id: int
    name: str
    description: str
    address: str
    main_photo: str
    another_photo: str
    start: datetime
    end: datetime


class EventCreate(BaseModel):
    town_id: int
    name: str
    description: Union[str, None] = None
    address: str
    main_photo: Union[str, None] = None
    another_photo: Union[str, None] = None
    start: datetime
    end: datetime


class EventUpdate(BaseModel):
    pass


class EventResponse(BaseModel):
    id: int


class EventListResponse(BaseModel):
    id: int | None = None
    town_id: int | None = None
    name: str | None = None
    address: str | None = None
    start: datetime | None = None
    end: datetime | None = None


class EventReplacementListResponse(BaseModel):
    id: int | None = None
    town_name: str | None = None
    name: str | None = None
    address: str | None = None
    start: datetime | None = None
    end: datetime | None = None