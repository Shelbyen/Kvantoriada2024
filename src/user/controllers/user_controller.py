from typing import Annotated, List

from fastapi import APIRouter, Request, Query, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.attraction_schema import (
    AttractionListResponse, AttractionCreate, AttractionResponse, AttractionReplacementListResponse
)
from ..schemas.event_schema import (
    EventReplacementListResponse, EventCreate, EventResponse
)
from ..schemas.town_schema import (
    TownListResponse
)
from ..schemas.category_schema import (
    CategoryListResponse
)

from ..services.attraction_service import attraction_service
from ..services.category_service import category_service
from ..services.town_service import town_service
from ..services.event_service import event_service


router = APIRouter()

templates = Jinja2Templates(directory="assets/templates")


@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="test.html"
    )


@router.get("/api/dev/get_all_attraction")
async def get_all_attraction(
        fields: Annotated[list, Query()] = None,
        order: Annotated[list, Query()] = None,
        limit: int | None = None,
        offset: int | None = None
) -> list[AttractionListResponse] | None:
    try:
        return await attraction_service.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/api/get_all_attraction")
async def get_all_attraction(
        town_ids: List[int] = Query(None),
        category_ids: List[int] = Query(None)
) -> list[AttractionReplacementListResponse] | None:
    target_attractions = await attraction_service.filter_with_replacement(
        town_ids=town_ids,
        category_ids=category_ids
    )
    try:
        all_towns = await town_service.get_all()
        all_category = await category_service.get_all()
        return list([AttractionReplacementListResponse(
            id=i.id,
            town_name=all_towns[i.town_id].name,
            category_name=all_category[i.category_id].name,
            name=i.name,
            description=i.description,
            address=i.address
        ) for i in target_attractions])
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/api/get_all_event")
async def get_all_event(
        town_ids: List[int] = Query(None)
) -> list[AttractionReplacementListResponse] | None:
    target_events = await event_service.filter_with_replacement(
        town_ids=town_ids
    )
    try:
        all_towns = await town_service.get_all()
        return list([EventReplacementListResponse(
            id=i.id,
            town_name=all_towns[i.town_id].name,
            name=i.name,
            description=i.description,
            address=i.address,
            start=i.start,
            end=i.end
        ) for i in target_events])
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))



@router.get("/api/get_all_towns")
async def get_all_towns() -> list[TownListResponse]:
    try:
        return await town_service.get_all()
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/api/get_all_categories")
async def get_all_towns() -> list[CategoryListResponse]:
    try:
        return await category_service.get_all()
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/api/dev/create_attraction")
async def create_attraction(
        data: AttractionCreate,
) -> AttractionResponse:
    try:
        return await attraction_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/api/dev/create_event")
async def create_event(
        data: EventCreate,
) -> EventResponse:
    try:
        return await event_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
