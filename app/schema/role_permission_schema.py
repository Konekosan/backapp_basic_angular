from typing import Optional
from pydantic import BaseModel, Field

class RolePermissionSchema(BaseModel):
    id_role: Optional[int]=None
    id_permission: Optional[int]=None

    class Config:
        orm_mode = True


class RequestRolePermission(BaseModel):
    parameter: RolePermissionSchema = Field(...)