from fastapi import APIRouter

from api.schemas.response import success_response
from api.services.compass_data import get_proposals


router = APIRouter(prefix="/proposals", tags=["Proposals"])


@router.get("")
def proposals():
    return success_response(get_proposals())
