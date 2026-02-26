import os
from sqlalchemy import create_engine

engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_pre_ping=True
)