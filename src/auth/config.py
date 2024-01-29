import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=r".env")

SECRET = os.environ.get("SECRET")
MAIL_FROM = os.environ.get("MAIL_FROM")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
