from fastapi import APIRouter

from api.schemas.response import success_response
from api.services.compass_data import get_market, get_market_sectors


router = APIRouter(prefix="/market", tags=["Market"])


@router.get("")
def market():
    return success_response(get_market())


@router.get("/sectors")
def sectors():
    return success_response(get_market_sectors())
