from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.controller import admin_repository
from app.app_config.database_config import get_db
from app.schema.role_schema import RequestRole
from app.schema.permission_schema import RequestPermission
from app.schema.role_usager_schema import RequestRoleUsager
from app.schema.role_permission_schema import RequestRolePermission

admin_router = APIRouter()

@admin_router.get("/roles")
async def get(db:Session=Depends(get_db)):
    _roles = admin_repository.fetch_roles(db, 0, 100)
    return _roles, 200

@admin_router.get("/permissions")
async def get(db:Session=Depends(get_db)):
    _permissions = admin_repository.fetch_permissions(db, 0, 100)
    return _permissions, 200

# Creation d'un role
@admin_router.post("/roles/add")
async def create(request: RequestRole, db:Session=Depends(get_db)):
    _roles = admin_repository.add_role(db, request.parameter)
    return _roles, 200

# Creation d'une permissions
@admin_router.post("/permissions/add")
async def create(request: RequestPermission, db:Session=Depends(get_db)):
    _permissions = admin_repository.add_permissions(db, request.parameter)
    return _permissions, 200

# assignation role sur un usager
@admin_router.post("/assign-role")
async def assign_role_to_user(request: RequestRoleUsager, db: Session = Depends(get_db)):
    _roles = admin_repository.assign_role_to_user(db, request.parameter)
    return _roles, 200

# assignation permission sur un role
@admin_router.post("/assign-permission")
async def assign_permission_to_role(request: RequestRolePermission, db: Session = Depends(get_db)):
    _permissions = admin_repository.assign_permission_to_role(db, request.parameter)
    return _permissions, 200