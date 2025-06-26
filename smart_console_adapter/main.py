from http.client import HTTPException
from os import getenv

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request

from .adapters.smart_console_adapter import SmartConsoleAdapter
from .config.settings import Settings
from .decorators.extract_session_id import extract_session_id
from .models.request_models import LoginRequest, SetUserRequest

load_dotenv()

app = FastAPI(
    title="Smart Console Adapter API",
    description="API adapter for Checkpoint's Smart Console",
    version="1.0.0",
)

api_base_url = getenv("API_BASE_URL")
domain = getenv("DOMAIN")
settings = Settings(api_base_url=api_base_url, domain=domain)

print("Settings loaded:")
print(f"API Base URL: {settings.api_base_url}")
print(f"Domain: {settings.domain}")


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
        return await adapter.login(credentials.user, credentials.password)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/show-users")
@extract_session_id
async def show_users(
    request: Request, adapter: SmartConsoleAdapter = Depends(get_adapter)
):
    try:
        response = await adapter.show_users()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/set-user")
@extract_session_id
async def set_user(
    _: Request,
    request_data: SetUserRequest,
    adapter: SmartConsoleAdapter = Depends(get_adapter),
):
    try:
        response = await adapter.set_user(
            name=request_data.name,
            details_level=request_data.details_level,
            expiration_days=request_data.expiration_days,
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
