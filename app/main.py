from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routers import health
from starlette import status

app = FastAPI(
    title="My API",
    version="0.1.0",
    description="My API description",
)
@app.get("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def root():
    return RedirectResponse(url="/docs")

app.include_router(health.router)