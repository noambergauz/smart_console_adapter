from fastapi import FastAPI
from src.routers.api import router

app = FastAPI(
    title="Smart Console Adapter API",
    description="API adapter for Checkpoint's Smart Console",
    version="1.0.0",
)

app.include_router(router, prefix="/api/v1", tags=["smart-console"])


@app.get("/")
async def root():
    return {"message": "Smart Console Adapter API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
