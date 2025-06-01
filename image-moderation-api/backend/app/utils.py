from fastapi import HTTPException, Header
from app.database import tokens_collection

def extract_token_from_header(auth_header: str):
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header.split()[1]
    return None

def validate_token(auth_header: str, require_admin: bool = False):
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    token = extract_token_from_header(auth_header)
    token_doc = tokens_collection.find_one({"token": token})
    if not token_doc:
        raise HTTPException(status_code=403, detail="Invalid token")
    if require_admin and not token_doc.get("isAdmin", False):
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return token_doc