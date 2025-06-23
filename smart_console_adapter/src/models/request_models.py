from typing import Optional, List

from pydantic import BaseModel


class ResourceRequest(BaseModel): ...


class CreateResourceRequest(ResourceRequest):
    name: str
    description: Optional[str] = None
    tags: List[str] = []


class UpdateResourceRequest(ResourceRequest):
    resource_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None


class DeleteResourceRequest(ResourceRequest):
    resource_id: str


class GetResourceRequest(ResourceRequest):
    resource_id: str


class ListResourcesRequest(ResourceRequest):
    limit: Optional[int] = 10
    offset: Optional[int] = 0
    filter: Optional[str] = None
