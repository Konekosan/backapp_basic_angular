from typing import Optional
from pydantic import BaseModel, Field

class RoleUsagerSchema(BaseModel):
    id_usager: Optional[int]=None
    id_role: Optional[int]=None

    class Config:
        orm_mode = True


class RequestRoleUsager(BaseModel):
    parameter: RoleUsagerSchema = Field(...)