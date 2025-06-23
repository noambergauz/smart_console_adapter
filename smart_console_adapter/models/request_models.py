from typing import Optional

from pydantic import BaseModel


class ResourceRequest(BaseModel): ...


class LoginRequest(ResourceRequest):
    user: str
    password: str


class SetUserRequest(ResourceRequest):
    name: str
    details_level: Optional[str] = "full"
    expiration_days: Optional[int] = 14
