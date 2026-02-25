import os
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY");
    JWT_ACCESS_COOKIE_NAME = "sessionId" 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "poolclass": NullPool,  
}
    
