from fastapi import APIRouter, HTTPException, Depends
from src.adapters.smart_console_adapter import SmartConsoleAdapter
from src.models.request_models import ResourceRequest
from src.models.response_models import ResourceResponse

router = APIRouter()


def get_adapter():
    # You should load these from environment variables or config
    return SmartConsoleAdapter(
        base_url="https://your-smart-console-url.com/api", api_key="your-api-key"
    )


@router.get("/resources/{resource_id}", response_model=ResourceResponse)
async def get_resource(
    resource_id: str, adapter: SmartConsoleAdapter = Depends(get_adapter)
):
    try:
        response = await adapter.get_resource(resource_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/resources", response_model=ResourceResponse)
async def create_resource(
    request: ResourceRequest, adapter: SmartConsoleAdapter = Depends(get_adapter)
):
    try:
        response = await adapter.create_resource(request.dict())
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
