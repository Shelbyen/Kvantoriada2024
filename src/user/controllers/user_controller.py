from typing import Annotated

from fastapi import APIRouter, Request, Query, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.attraction_schema import (
    AttractionListResponse, AttractionCreate, AttractionResponse, AttractionReplacementListResponse
)
from ..schemas.town_schema import (
    TownListResponse
)

from ..services.attraction_service import attraction_service
from ..services.town_service import town_service

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
        town_ids: list[int] | None = None,
        category_ids: list[int] | None = None
) -> list[AttractionReplacementListResponse] | None:
    try:
        target_attraction = await attraction_service.filter_with_replacement(
            town_ids=town_ids,
            category_ids=category_ids
        )
        all_towns = await town_service.get_all()

    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/api/get_all_towns")
async def get_all_towns() -> list[TownListResponse]:
    try:
        return await town_service.get_all()
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/api/get_all_categories")
async def get_all_towns() -> list[TownListResponse]:
    try:
        return await town_service.get_all()
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
