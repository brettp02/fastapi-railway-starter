from logging.config import dictConfig


def configure_logging(level: str = "info") -> None:
    log_level = level.upper()

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                }
            },
            "root": {"level": "WARNING", "handlers": ["default"]},
            "loggers": {
                "app": {
                    "level": log_level,
                    "handlers": ["default"],
                    "propagate": False,
                },
                "uvicorn.access": {
                    "level": log_level,
                    "handlers": ["default"],
                    "propagate": False,
                },
                "uvicorn.error": {
                    "level": log_level,
                    "handlers": ["default"],
                    "propagate": False,
                },
            },
        }
    )
