from fastapi import APIRouter, File, UploadFile, Header
from datetime import datetime
from app.utils import validate_token
from app.database import usages_collection

moderate_router = APIRouter()

@moderate_router.post("/moderate")
def moderate_image(file: UploadFile = File(...), authorization: str = Header(...)):
    token_doc = validate_token(authorization)

    # Simulated moderation logic (replace with ML model or API call)
    result = {
        "nudity": 0.85,
        "violence": 0.10,
        "self_harm": 0.02,
        "hate_symbols": 0.00
    }

    # Track usage
    usages_collection.insert_one({
        "token": token_doc["token"],
        "endpoint": "/moderate",
        "timestamp": datetime.utcnow()
    })

    return {"filename": file.filename, "result": result}