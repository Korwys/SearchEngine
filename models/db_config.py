import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
ip = os.getenv('DB_ADRESS')
dbname = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{ip}/{dbname}"
ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{ip}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
