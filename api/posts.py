import json

from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from models.db_config import get_db
from schemas.posts import PostInDB
from services.crud import get_search_results_by_text, delete_id_in_elastic, delete_id_in_db
from services.redis_cache import redis_cache
from services.settings import manager

router = APIRouter()


@router.get('/search/{query}', response_model=list[PostInDB], status_code=status.HTTP_200_OK)
async def get_results(query: str, session: AsyncSession = Depends(get_db)) -> list[PostInDB]:
    """Возвращает упорядочный список результатов поиска"""
    if manager.redis.get(query):
        return json.loads(manager.redis.get(query))
    else:
        response = await get_search_results_by_text(data=query, session=session)
        redis_cache(response, query)
        return response


@router.delete('/delete/{post_id}', status_code=status.HTTP_200_OK)
async def delete_id(id: int, session: AsyncSession = Depends(get_db)) -> JSONResponse:
    """Удаляет данные по ID из ElasticSearch и БД"""
    await delete_id_in_elastic(id=id)
    await delete_id_in_db(id=id, session=session)
    return JSONResponse(status_code=200, content={"message": "Object deleted"})
