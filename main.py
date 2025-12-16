from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Email Spam Detector is running"}
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
import os

app = FastAPI()

# OAuth configuration
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
REDIRECT_URI = "http://localhost:8000/auth/callback"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # local dev only


@app.get("/")
def home():
    return {"message": "AI Email Spam Detector running"}


@app.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )

    authorization_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )

    return RedirectResponse(authorization_url)


@app.get("/auth/callback")
def auth_callback(request: Request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )

    flow.fetch_token(authorization_response=str(request.url))
    credentials = flow.credentials

    return {
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "scopes": credentials.scopes,
    }
