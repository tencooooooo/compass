from fastapi import APIRouter, HTTPException

from api.schemas.response import success_response
from api.services.compass_data import get_companies, get_company


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("")
def list_companies():
    return success_response(get_companies())


@router.get("/{ticker}")
def company_detail(ticker: str):
    company = get_company(ticker)
    if company is None:
        raise HTTPException(status_code=404, detail=f"Company not found: {ticker.upper()}")
    return success_response(company)
