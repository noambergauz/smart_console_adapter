from os import environ
from http.client import HTTPException
from fastapi import FastAPI, Depends, APIRouter

from smart_console_adapter.adapters.smart_console_adapter import SmartConsoleAdapter
from smart_console_adapter.models.request_models import LoginRequest, SetUserRequest
from smart_console_adapter.config.settings import Settings

app = FastAPI(
    title="Smart Console Adapter API",
    description="API adapter for Checkpoint's Smart Console",
    version="1.0.0",
)

router = APIRouter()

app.include_router(router, prefix="/api/v1", tags=["smart-console"])


api_base_url = environ.get("API_BASE_URL")
domain = environ.get("DOMAIN")
settings = Settings(api_base_url=api_base_url, domain=domain)


def get_adapter():
    return SmartConsoleAdapter(base_url=settings.api_base_url, domain=settings.domain)


@app.get("/")
async def root():
    return {"message": "Smart Console Adapter API is running"}


@app.post("/login")
async def login(
    credentials: LoginRequest, adapter: SmartConsoleAdapter = Depends(get_adapter)
):
    try:
        response = await adapter.login(credentials.user, credentials.password)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/show-users")
async def show_users(adapter: SmartConsoleAdapter = Depends(get_adapter)):
    try:
        response = await adapter.show_users()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/set-user")
async def set_user(
    request: SetUserRequest,
    adapter: SmartConsoleAdapter = Depends(get_adapter),
):
    try:
        response = await adapter.set_user(
            name=request.name,
            details_level=request.details_level,
            expiration_days=request.expiration_days,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
