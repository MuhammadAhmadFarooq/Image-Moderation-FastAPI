from fastapi import FastAPI, Request
from app.auth import auth_router
from app.moderate import moderate_router
from app.database import usages_collection
from datetime import datetime
from app.utils import extract_token_from_header

app = FastAPI(title="Image Moderation API")

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(moderate_router, tags=["Moderation"])

@app.middleware("http")
async def log_usage(request: Request, call_next):
    token = extract_token_from_header(request.headers.get("authorization", ""))
    if token:
        usages_collection.insert_one({
            "token": token,
            "endpoint": request.url.path,
            "timestamp": datetime.utcnow()
        })
    response = await call_next(request)
    return response