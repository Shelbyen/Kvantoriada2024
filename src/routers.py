from fastapi import APIRouter

from .user.controllers import user_controller


def get_apps_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    return router
