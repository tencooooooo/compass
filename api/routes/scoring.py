from fastapi import APIRouter, HTTPException

from api.schemas.response import success_response
from api.services.compass_data import get_score, get_scores


router = APIRouter(prefix="/scores", tags=["Scoring"])


@router.get("")
def scores():
    return success_response(get_scores())


@router.get("/{ticker}")
def score_detail(ticker: str):
    try:
        score = get_score(ticker)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ticker")
    if score is None:
        raise HTTPException(status_code=404, detail=f"Score not found: {ticker.upper()}")
    return success_response(score)
