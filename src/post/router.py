import json
import logging

from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from config.db import get_db
from post.schemas import PostInDB
from post.services import get_search_results_by_text, delete_id_in_elastic, delete_id_in_db, delete_from_cache
from post.cache import redis_cache
from config.setup_manager import manager

router = APIRouter()

logger = logging.getLogger('app.api.post')


@router.get('/search/{query}', response_model=list[PostInDB], status_code=status.HTTP_200_OK)
async def get_results(query: str, session: AsyncSession = Depends(get_db)) -> list[PostInDB]:
    """Возвращает упорядочный список результатов поиска"""
    try:
        if manager.redis.get(query):
            return json.loads(manager.redis.get(query))
        else:
            response = await get_search_results_by_text(data=query, session=session)
            redis_cache(response, query)
            return response
    except Exception as err:
        logger.exception(err)

@router.delete('/delete/{post_id}', status_code=status.HTTP_200_OK)
async def delete_id(id: int, session: AsyncSession = Depends(get_db)) -> JSONResponse:
    """Удаляет данные по ID из ElasticSearch и БД"""
    await delete_id_in_elastic(id=id)
    await delete_id_in_db(id=id, session=session)
    await delete_from_cache()
    return JSONResponse(status_code=200, content={"message": "Object deleted"})
