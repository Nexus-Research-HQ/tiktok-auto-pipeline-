from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app_core import TikTokAppBackendEngine

app = FastAPI(title="TikTok Auto Pipeline API")
engine = TikTokAppBackendEngine()

class UserRegistration(BaseModel):
    username: str
    country: str

class WithdrawalRequest(BaseModel):
    username: str
    method: str
    destination: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend pipeline engine operational"}

@app.post("/register")
def register_user(data: UserRegistration):
    result = engine.register_user(data.username, data.country)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/view")
def log_view(username: str):
    result = engine.log_video_view(username)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.post("/withdraw")
def withdraw(data: WithdrawalRequest):
    result = engine.process_withdrawal(data.username, data.method, data.destination)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
