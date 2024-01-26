import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=r".env")

SECRET = os.environ.get("SECRET")