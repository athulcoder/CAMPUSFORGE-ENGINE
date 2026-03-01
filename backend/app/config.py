import os
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
class Config:

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB

    MINIO_ENDPOINT = "minio:9000"
    MINIO_ACCESS_KEY = "minioadmin"
    MINIO_SECRET_KEY = "minioadmin123"
    MINIO_SECURE = False
    RESUME_BUCKET = "resumes"

    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY");
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_SAMESITE = "None"

    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"