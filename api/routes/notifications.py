from fastapi import APIRouter

from api.schemas.response import success_response
from api.services.compass_data import get_notifications


router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("")
def notifications():
    return success_response(get_notifications())
