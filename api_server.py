from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app_core import TikTokAppBackendEngine

app = FastAPI(title="TikTok Payout App API", version="1.0")
engine = TikTokAppBackendEngine()

class RegisterRequest(BaseModel):
    username: str
    country: str

class ViewRequest(BaseModel):
    username: str

class WithdrawalRequest(BaseModel):
    username: str
    method: str
    destination: str

@app.post("/api/register")
def register(data: RegisterRequest):
    result = engine.register_user(data.username, data.country)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/api/video/view")
def log_view(data: ViewRequest):
    result = engine.log_video_view(data.username)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/api/wallet/withdraw")
def withdraw(data: WithdrawalRequest):
    result = engine.process_withdrawal(data.username, data.method, data.destination)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
