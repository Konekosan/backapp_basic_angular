from typing import Optional
from pydantic import BaseModel, Field

class RoleSchema(BaseModel):
    id: Optional[int]=None
    nom: Optional[str]=None

    class Config:
        orm_mode = True


class RequestRole(BaseModel):
    parameter: RoleSchema = Field(...)