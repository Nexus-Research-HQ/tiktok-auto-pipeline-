from fastapi import FastAPI

app = FastAPI(title="TikTok Auto Pipeline API")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend pipeline engine operational"}
