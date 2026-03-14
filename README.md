# FastAPI Railway Starter

Minimal FastAPI starter template for small backend services, internal tools, ML/AI APIs, and data-focused projects. Managed with `uv` and deployable to Railway in minutes.

[![CI](https://github.com/brettp02/fastapi-railway-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/brettp02/fastapi-railway-starter/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-009688?logo=fastapi&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-deploy%20ready-0B0D0E?logo=railway&logoColor=white)
![uv](https://img.shields.io/badge/managed%20with-uv-6E56CF)
![Ruff](https://img.shields.io/badge/lint-ruff-D7FF64?logo=ruff&logoColor=000000)

## Deploy In Minutes

This template is designed to be deployed to Railway with almost no setup.

Basic flow:

1. Clone this repo.
2. Push it to your own GitHub repository.
3. Log in to Railway with GitHub.
4. Create a new project from the GitHub repo.
5. In Railway settings, add a public networking domain for port `8080`.
6. Your app should be live.

For the default starter app, that can take only a few minutes.

The included `railway.toml` already starts the app with:

```toml
[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
```

Once deployed, Railway should serve:

- `/docs`
- `/health`

## What This Includes

- FastAPI app with a health endpoint
- Railway-ready `uvicorn` startup command
- Environment-driven settings via `pydantic-settings`
- Basic stdout logging suitable for Railway
- `pytest` and `ruff` wired in

## Project Structure

```text
app/
  api/
    routers/
  core/
  schemas/
  services/
tests/
```

- `app/api/routers/` contains FastAPI route modules and endpoint definitions.
- `app/core/` contains application-wide setup such as settings, logging, and shared infrastructure code.
- `app/schemas/` is a place for Pydantic request and response models as the API grows.
- `app/services/` is a place for application logic such as model loading, inference code, third-party API clients, database operations, or other reusable business logic.
- `tests/` contains the test suite.

You do not need to use every directory immediately. They are included as sensible starting points, not rigid rules.

## Quick Start

If you are already inside the repo:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`

## Local Setup

If you want the full local setup flow:

```bash
git clone 'https://github.com/brettp02/fastapi-railway-starter.git'
cd fastapi-railway-starter
uv sync
uv run uvicorn app.main:app --reload
```

## Development Commands

```bash
uv run pytest
uv run ruff check .
```

## Configuration

Application settings live in `app/core/config.py`.

The values defined there are local-safe defaults, not production values. They exist so the starter runs immediately without extra setup.

Override settings with environment variables using the `APP_` prefix, either in a local `.env` file or through your deployment platform:

```env
APP_APP_NAME=FastAPI Railway Starter
APP_APP_DESCRIPTION=Minimal FastAPI starter template
APP_ENVIRONMENT=local
APP_DEBUG=false
APP_LOG_LEVEL=info
```

The repo includes `.env.example` as the reference file for supported variables.

### Important

For production deployments, prefer setting environment variables in Railway instead of editing the defaults in `app/core/config.py`.

Typical Railway values:

```env
APP_ENVIRONMENT=production
APP_LOG_LEVEL=info
```

You can also override:

- `APP_APP_NAME`
- `APP_APP_DESCRIPTION`
- `APP_DEBUG`

## Deployment

Railway starts the app using `railway.toml`:

```toml
[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
```

As long as your Railway service has the required env vars, no code changes are needed for deployment.
