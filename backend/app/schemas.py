### backend/app/schemas.py
from pydantic import BaseModel
from datetime import datetime


class TokenOut(BaseModel):
    token: str
    isAdmin: bool
    createdAt: datetime


class ModerateResponse(BaseModel):
    filename: str
    result: dict[str, float]
