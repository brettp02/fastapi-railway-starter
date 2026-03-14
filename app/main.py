from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routers import health

app = FastAPI(
    title="My API",
    version="0.1.0",
    description="My API description",
)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

app.include_router(health.router)