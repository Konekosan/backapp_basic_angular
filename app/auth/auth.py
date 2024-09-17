from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from app.app_config.config import (
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
)
from app.model.token import  TokenEnum, TokenData
from jose import  jwt

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

# Creation du access token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=int(JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update(
        {"exp": int(expire.timestamp()), "token_data": TokenEnum.AccessToken.value}
    )

    return jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)

# Vérification du token
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        id = payload.get("usager_id")

        if id is None:
            raise credentials_exception

        token_data = TokenData(id=str(id), **payload)

    except jwt.JWTError:
        raise credentials_exception

    return token_data