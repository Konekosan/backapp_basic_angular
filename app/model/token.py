from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenEnum(Enum):
    RefreshToken = "refresh_token"
    AccessToken = "access_token"

class TokenData(BaseModel):
    id: Optional[str]
    token_data: Optional[TokenEnum]


class TokenTest(BaseModel):
    id: Optional[str]