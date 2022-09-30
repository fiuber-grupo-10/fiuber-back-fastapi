from functools import cache

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


def create_engine_from_url(db_url: str):
    return create_engine(
        db_url,
        connect_args={"check_same_thread": False},
        echo=True
    )


def create_session_from_url(db_url: str):
    engine = create_engine(db_url)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
