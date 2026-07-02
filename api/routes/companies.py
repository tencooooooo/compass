from fastapi import APIRouter, HTTPException

from api.schemas.response import success_response
from api.services.compass_data import get_companies, get_company


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("")
def list_companies():
    return success_response(get_companies())


@router.get("/{ticker}")
def company_detail(ticker: str):
    try:
        company = get_company(ticker)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ticker")
    if company is None:
        raise HTTPException(status_code=404, detail=f"Company not found: {ticker.upper()}")
    return success_response(company)
