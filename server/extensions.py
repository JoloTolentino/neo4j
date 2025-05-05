import logging
from fastapi import Request, Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session, sessionmaker, declarative_base
import os


Base = declarative_base()
base_dir = os.path.dirname(os.path.abspath(__file__))
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
logger_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logs_dir = os.path.join(base_dir, "logs")
formatter = logging.Formatter(logger_fmt)
file_handler = logging.FileHandler(os.path.join(logs_dir, f"{__name__}.log"))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
error_handler = logging.FileHandler(os.path.join(logs_dir, f"{__name__}_errors.log"))
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)
LOGGER.addHandler(error_handler)
LOGGER.addHandler(stream_handler)

# DB_URL = "postgresql+psycopg2://jolo@localhost:5432/study" #sync
DB_URL = 'postgresql+asyncpg://jolo@localhost:5432/study'
engine = create_async_engine(DB_URL)




# sync 
# engine = create_engine(DB_URL)


#sync 
#flush is being able to query your transactions that havent been committed yet 
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False,bind= engine)


async def get_pg_session():


    
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
