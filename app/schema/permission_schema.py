from typing import Optional, TypeVar
from pydantic import BaseModel, Field

class PermissionsSchema(BaseModel):
    id: Optional[int]=None
    nom: Optional[str]=None

    class Config:
        orm_mode = True

class RequestPermission(BaseModel):
    parameter: PermissionsSchema = Field(...)