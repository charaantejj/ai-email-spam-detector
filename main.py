from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Email Spam Detector is running"}
