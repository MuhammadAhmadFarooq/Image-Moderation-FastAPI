from datetime import datetime
from pydantic import BaseModel

class TokenModel(BaseModel):
    token: str
    isAdmin: bool
    createdAt: datetime

class UsageModel(BaseModel):
    token: str
    endpoint: str
    timestamp: datetime
