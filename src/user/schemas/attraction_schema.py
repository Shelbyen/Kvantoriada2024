from typing import Union

from pydantic import BaseModel


class AttractionBase(BaseModel):
    id: int
    town_id: int
    category_id: int
    name: str
    description: str
    address: str
    main_photo: str
    another_photo: str


class AttractionCreate(BaseModel):
    id: int
    town_id: int
    category_id: int
    name: str
    description: Union[str, None] = None
    address: Union[str, None] = None
    main_photo: Union[str, None] = None
    another_photo: Union[str, None] = None


class AttractionUpdate(BaseModel):
    pass


class AttractionResponse(BaseModel):
    id: int


class AttractionListResponse(BaseModel):
    id: Union[int, None] = None
    town_id: Union[int, None] = None
    category_id: Union[int, None] = None
    name: Union[str, None] = None
    description: Union[str, None] = None
    address: Union[str, None] = None


class AttractionReplacementListResponse(BaseModel):
    id: Union[int, None] = None
    town_name: Union[str, None] = None
    category_name: Union[str, None] = None
    name: Union[str, None] = None
    description: Union[str, None] = None
    address: Union[str, None] = None

