from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schema.auth_schema import (
    LoginResponseSchema
)
from typing import Annotated
from sqlalchemy.orm import Session
from app.app_config.database_config import get_db
from app.controller import usager_repository
from app.auth.auth import create_access_token, create_refresh_token, get_current_usager
from app.model.usager import Usager
from app.schema.usager_schema import UsagerSchema

login_router = APIRouter()

@login_router.post("", response_model=LoginResponseSchema)
async def login(payload: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):

    user = usager_repository.fetch_user_by_username(db, payload.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials."
        )
    
    access_token = create_access_token(data={"usager_id": user.id})
    refresh_token = create_refresh_token(data={"usager_id": user.id})

    return LoginResponseSchema(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )

# Return current usager if logged
@login_router.get("/me")
async def get_me(user: Usager = Depends(get_current_usager), db: Session = Depends(get_db)) -> UsagerSchema:
    if not user or (user.id is None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials."
        )
    return user