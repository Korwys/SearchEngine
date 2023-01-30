from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.base import settings

SQLALCHEMY_DATABASE_URL = \
    f"postgresql+asyncpg://{settings.db_username}:{settings.db_password}@{settings.db_address}/{settings.db_name}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with async_session() as db:
        yield db
        await db.commit()
