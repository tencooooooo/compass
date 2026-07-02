from fastapi import APIRouter, HTTPException

from api.schemas.response import success_response
from api.services.compass_data import get_validation, get_validation_for_ticker


router = APIRouter(prefix="/validation", tags=["Validation"])


@router.get("")
def validation():
    return success_response(get_validation())


@router.get("/{ticker}")
def validation_for_ticker(ticker: str):
    try:
        return success_response(get_validation_for_ticker(ticker))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ticker")
