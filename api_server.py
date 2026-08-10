from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app_core import TikTokAppBackendEngine

app = FastAPI()
engine = TikTokAppBackendEngine()

class UserRegister(BaseModel):
    username: str
    country: str

class WithdrawalRequest(BaseModel):
    username: str
    method: str
    destination: str

@app.get("/")
def read_root():
    return {"status": "online", "service": "TikTok Backend Engine"}

@app.post("/register")
def register_user(data: UserRegister):
    try:
        result = engine.register_user(data.username, data.country)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/view")
def log_view(username: str):
    try:
        result = engine.log_video_view(username)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/withdraw")
def withdraw(data: WithdrawalRequest):
    try:
        result = engine.process_withdrawal(data.username, data.method, data.destination)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
