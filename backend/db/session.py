from sqlalchemy.orm import sessionmaker
from db.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)