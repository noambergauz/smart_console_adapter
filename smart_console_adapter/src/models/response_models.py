from typing import Any, List, Optional

from pydantic import BaseModel


class ResourceResponse(BaseModel):
    success: bool
    message: Optional[str] = None


class DataResponseModel(ResourceResponse):
    data: Any


class ListResponseModel(ResourceResponse):
    items: List[Any]


class ErrorResponseModel(ResourceResponse):
    error_code: str
    error_details: Optional[str] = None
