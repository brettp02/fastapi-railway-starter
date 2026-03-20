from fastapi import APIRouter

from app.api.routers import health

# All routers are registered here and exposed as a single api_router.
# main.py includes api_router once, so new routers only need to be added here.
api_router = APIRouter()
api_router.include_router(health.router)
