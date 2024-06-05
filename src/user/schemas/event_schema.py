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
    pass


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
