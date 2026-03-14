import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.routers import health
from app.core.config import get_settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)
    logger = logging.getLogger("app")

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        logger.info(
            "Starting %s in %s environment",
            settings.app_name,
            settings.environment,
        )
        yield
        logger.info("Shutting down %s", settings.app_name)

    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        debug=settings.debug,
        lifespan=lifespan,
    )

    @app.get("/", include_in_schema=False)
    async def root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    app.include_router(health.router)
    return app


app = create_app()
