from fastapi import APIRouter, Header, HTTPException
from uuid import uuid4
from datetime import datetime
from app.database import tokens_collection
from app.utils import validate_token

auth_router = APIRouter()

@auth_router.post("/tokens")
def create_token(authorization: str = Header(...)):
    validate_token(authorization, require_admin=True)
    new_token = str(uuid4())
    tokens_collection.insert_one({
        "token": new_token,
        "isAdmin": False,
        "createdAt": datetime.utcnow()
    })
    return {"token": new_token}

@auth_router.get("/tokens")
def list_tokens(authorization: str = Header(...)):
    validate_token(authorization, require_admin=True)
    tokens = list(tokens_collection.find({}, {"_id": 0}))
    return tokens

@auth_router.delete("/tokens/{token}")
def delete_token(token: str, authorization: str = Header(...)):
    validate_token(authorization, require_admin=True)
    result = tokens_collection.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"message": "Token deleted"}