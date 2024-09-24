import logging

from sqlalchemy.orm import Session
from app.model.usager import Role, Permission, Usager
from fastapi import HTTPException, status
from app.schema.role_usager_schema import RoleUsagerSchema
from app.schema.role_schema import RoleSchema
from app.schema.permission_schema import PermissionsSchema
from app.schema.role_permission_schema import RolePermissionSchema

loggers = logging.getLogger(__name__)

#Logger
def _print(text: str, log_level='info'):
    print(text)
    getattr(loggers, log_level)(text)

# Get all roles
def fetch_roles(db:Session, skipt:int=0, limit:int=100):
    return db.query(Role).offset(skipt).limit(limit).all()

# Get all permissions
def fetch_permissions(db:Session, skipt:int=0, limit:int=100):
    return db.query(Permission).offset(skipt).limit(limit).all()

# Create role
def add_role(db:Session, role: RoleSchema):
    _role = Role(nom=role.nom)
    db.add(_role)
    try:
        db.commit()
        db.refresh(_role)
        _print('Role ajouté avec succès !')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return _role

# Create permission
def add_permissions(db:Session, permission: PermissionsSchema):
    _permission = Permission(nom=permission.nom)
    db.add(_permission)
    try:
        db.commit()
        db.refresh(_permission)
        _print('Permissions ajoutée avec succès !')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return _permission

# Assign role to usager
def assign_role_to_user(db:Session, role_user: RoleUsagerSchema):

    usager = db.query(Usager).filter(Usager.id == role_user.id_usager).first()
    role = db.query(Role).filter(Role.id == role_user.id_role).first()
    
    if not usager:
            raise HTTPException(status_code=404, detail="Usager not found")
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    try:
        if role not in usager.roles:
            usager.roles.append(role)
            _print(usager)
            db.commit()
            _print('Role ajouté avec succès !')
        _print(usager)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return {"message": "Role assigned successfully"}

# Get permissions from user
def get_user_permissions(user_id: int, db: Session):
    user = db.query(Usager).filter(Usager.id == user_id).first()

    if not user:
        return []

    permissions = set()

    for role in user.roles:
        for permission in role.permissions:
            permissions.add(permission.nom)
    
    return list(permissions)

# Assign permission to role
def assign_permission_to_role(db:Session, role_permissions: RolePermissionSchema):

    permission = db.query(Permission).filter(Permission.id == role_permissions.id_permission).first()
    role = db.query(Role).filter(Role.id == role_permissions.id_role).first()

    if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    try:
        if permission not in role.permissions:
            role.permissions.append(permission)
            db.commit()
        _print('Permission ajoutée avec succès !')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'ajout",
        )
    return {"message": "Permission assigned successfully"}