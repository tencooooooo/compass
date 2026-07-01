from fastapi import APIRouter

from api.schemas.response import success_response
from api.services.compass_data import get_learning


router = APIRouter(prefix="/learning", tags=["Learning"])


@router.get("")
def learning():
    return success_response(get_learning())
