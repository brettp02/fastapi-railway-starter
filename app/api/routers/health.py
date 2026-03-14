from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/health"
)

@router.get("/", status_code=status.HTTP_200_OK)
async def health():
    return {"status": "ok"}