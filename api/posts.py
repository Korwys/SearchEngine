import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_config import get_db
from schemas.posts import PostInDB

router = fastapi.APIRouter()


@router.get('/', response_model=PostInDB)
async def get_results(db: AsyncSession = Depends(get_db)):
    pass


@router.delete('/{article_id}')
async def delete_article_from_db_and_elastic(article_id: int, db: AsyncSession = Depends(get_db)):
    pass
