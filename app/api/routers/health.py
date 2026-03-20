from fastapi import APIRouter
from starlette import status

from app.schemas.health import HealthResponse

router = APIRouter(
    prefix="/health"
)


@router.get("", status_code=status.HTTP_200_OK, response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok")