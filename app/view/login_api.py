from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schema.auth_schema import (
    LoginResponseSchema
)
from typing import Annotated
from sqlalchemy.orm import Session
from app.app_config.database_config import get_db

login_router = APIRouter()

@login_router.post("/login", response_model=LoginResponseSchema)
async def login(payload: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    print('coucou')