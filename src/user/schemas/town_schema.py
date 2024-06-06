from pydantic import BaseModel


class TownBase(BaseModel):
    id: int
    name: str


class TownCreate(BaseModel):
    pass


class TownUpdate(BaseModel):
    pass


class TownResponse(BaseModel):
    id: int


class TownListResponse(BaseModel):
    id: int | None = None
    name: str | None = None
