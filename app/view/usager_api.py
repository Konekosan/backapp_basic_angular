from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schema.auth_schema import (
    LoginResponseSchema
)
from typing import Annotated
from sqlalchemy.orm import Session
from app.app_config.database_config import get_db
from app.schema.usager_schema import RequestUser
from app.controller import usager_repository

usager_router = APIRouter()

# Fetch all usagers
@usager_router.get("/")
async def get(db:Session=Depends(get_db)):
    _user = usager_repository.get_users(db, 0, 100)
    return _user, 200

# Creation d'un usager
@usager_router.post("/create")
async def create(request: RequestUser, db:Session=Depends(get_db)):
    _user = usager_repository.add_user(db, request.parameter)
    return _user, 200

# Get usager by id
@usager_router.get("/{id}")
async def get_by_id(id: int, db:Session=Depends(get_db)):
    _user = usager_repository.fetch_user_by_id(db, id)
    return _user, 200

# Delete usager by id
@usager_router.delete("/{id}")
def delete(id: int, db:Session=Depends(get_db)):
    usager_repository.remove_user(db, id)
    return 200