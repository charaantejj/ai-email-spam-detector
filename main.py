from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from services.gmail_services import get_gmail_service, read_email_body
from ml.predict import predict_spam
import os

app = FastAPI()

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
REDIRECT_URI = "http://localhost:8000/auth/callback"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Temporary in-memory storage (we'll improve later)
user_credentials = None


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

    auth_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )

    return RedirectResponse(auth_url)


@app.get("/auth/callback")
def auth_callback(request: Request):
    global user_credentials

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )

    flow.fetch_token(authorization_response=str(request.url))
    user_credentials = flow.credentials

    return RedirectResponse("/emails")


@app.get("/emails")
def fetch_emails():
    if not user_credentials:
        return {"error": "User not authenticated"}

    creds = Credentials(
        token=user_credentials.token,
        refresh_token=user_credentials.refresh_token,
        token_uri=user_credentials.token_uri,
        client_id=user_credentials.client_id,
        client_secret=user_credentials.client_secret,
        scopes=user_credentials.scopes,
    )

    service = get_gmail_service(creds)

    results = service.users().messages().list(
        userId="me",
        maxResults=5
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for msg in messages:
        message = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        headers = message["payload"]["headers"]
        subject = sender = ""

        for h in headers:
            if h["name"] == "Subject":
                subject = h["value"]
            if h["name"] == "From":
                sender = h["value"]

        body = read_email_body(message)

        prediction = predict_spam(body)

    emails.append({
            "from": sender,
            "subject": subject,
            "spam": prediction["label"],
            "confidence": prediction["confidence"],
            "preview": body[:200]
    })
    return emails
