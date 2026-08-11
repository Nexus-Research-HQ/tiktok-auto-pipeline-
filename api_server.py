from fastapi import FastAPI, HTTPException, Security, Header
from fastapi.security.api_key import APIKeyHeader
from app_core import TikTokAppBackendEngine

app = FastAPI(title="TikTok Automation Backend")
engine = TikTokAppBackendEngine()

API_KEY = "my_secret_backend_key_123"  # In production, load this from environment variables
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate credentials / Invalid API Key")
    return api_key

@app.post("/register")
def register(username: str, country: str, api_key: str = Security(verify_api_key)):
    return engine.register_user(username, country)

@app.post("/view")
def log_view(username: str, api_key: str = Security(verify_api_key)):
    return engine.log_video_view(username)

@app.post("/withdraw")
def withdraw(username: str, method: str, destination: str, api_key: str = Security(verify_api_key)):
    return engine.process_withdrawal(username, method, destination)
