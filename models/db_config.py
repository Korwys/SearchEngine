import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
ip = os.getenv('DB_ADRESS')
dbname = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{ip}/{dbname}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as db:
        yield db
        await db.commit()
