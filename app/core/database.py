from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from app.core.config import Settings

DATABASE_URL = Settings.DATABASE_URL
print("DB URL:", DATABASE_URL)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
