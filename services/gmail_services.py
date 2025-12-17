from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import base64


def get_gmail_service(credentials):
    service = build("gmail", "v1", credentials=credentials)
    return service


def read_email_body(message):
    payload = message["payload"]
    parts = payload.get("parts")

    if parts:
        for part in parts:
            if part["mimeType"] == "text/plain":
                data = part["body"]["data"]
                text = base64.urlsafe_b64decode(data).decode("utf-8")
                return text
            elif part["mimeType"] == "text/html":
                data = part["body"]["data"]
                html = base64.urlsafe_b64decode(data).decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")
                return soup.get_text()

    return ""
