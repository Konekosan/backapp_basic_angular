from pydantic import BaseModel
from typing import Optional
from app.model.token import TokenData


class RefreshTokenRequestSchema(BaseModel):
    refresh_token: str


class RefreshTokenResponseSchema(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
    token_data: Optional[TokenData]


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str