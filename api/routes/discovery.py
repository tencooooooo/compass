from fastapi import APIRouter

from api.schemas.response import success_response
from api.services.compass_data import get_discovery, get_top_discovery


router = APIRouter(prefix="/discovery", tags=["Discovery"])


@router.get("")
def discovery():
    return success_response(get_discovery())


@router.get("/top")
def top_discovery(limit: int = 3):
    return success_response(get_top_discovery(limit=max(1, min(limit, 20))))
