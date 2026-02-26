from sqlalchemy.orm import sessionmaker
from backend.db.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)