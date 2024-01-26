import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=r".env")

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_schema = os.environ.get("DB_SCHEMA")
