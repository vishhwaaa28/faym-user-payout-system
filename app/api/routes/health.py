from fastapi import APIRouter

from app.schemas.common import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("", response_model=HealthResponse)
def health_check():
    return HealthResponse(status="ok")