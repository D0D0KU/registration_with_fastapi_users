from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

from fastapi.templating import Jinja2Templates

from src.auth.config import SECRET, MAIL_FROM, MAIL_PASSWORD
import jwt


class EmailSchema(BaseModel):
    email: List[EmailStr]

templates = Jinja2Templates(directory="src/templates")

conf = ConnectionConfig(
    MAIL_USERNAME = MAIL_FROM,
    MAIL_PASSWORD = MAIL_PASSWORD,
    MAIL_FROM = MAIL_FROM,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME=MAIL_FROM,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


async def simple_send(email: EmailSchema, id: int, username: str) -> JSONResponse:
    token_data = {
        "id": id,
        "username": username
    }
    token = jwt.encode(token_data, SECRET)

    # Insert the token into the template context
    context = {"request": None, "token": token}

    # Use TemplateResponse to insert a token into a template
    html_content = templates.TemplateResponse("auth/verification.html", context).body

    message = MessageSchema(
        subject="Verification",
        recipients=email.dict().get("email"),
        body=html_content,
        subtype=MessageType.html)
    
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


def very_token(token: str, secret_string: str = SECRET):

    payload = jwt.decode(token, secret_string, algorithms=['HS256'])

    return payload
