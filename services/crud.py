import logging

from elasticsearch import exceptions as Exp
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import OperationalError, NoResultFound, DisconnectionError, DatabaseError

from models.posts import Post
from config.setup_manager import manager


logger =logging.getLogger('app.services.crud')

async def get_search_results_by_text(data: str, session: AsyncSession):
    """Возвращает результы поискового запроса"""
    try:
        elastic_query = await manager.async_elastic_client.search(
            index="posts",
            body={"size": 1500, "query": {"match": {"text": data}}}
        )
        list_id = [item['_source']['id'] for item in elastic_query['hits']['hits']]
        new_query = list(map(int, list_id))
        result = await session.execute(
            select(Post).where(Post.id.in_(new_query)).order_by(Post.created_date.desc()).limit(20))
        return result.scalars().all()
    except Exception as err:
        logger.exception(err)


async def delete_id_in_elastic(id: int) -> None:
    """Удаляет документы из elastica по ID"""
    try:
        fetch_element_by_id = await manager.async_elastic_client.search(
            index='posts',
            body={"size": 1, "query": {"match": {"id": id}}}
        )
        elastic_id = fetch_element_by_id['hits']['hits'][0]['_id']
        await manager.async_elastic_client.delete(index='posts', id=elastic_id)
    except Exception as err:
        logger.exception(err)


async def delete_id_in_db(id: int, session: AsyncSession) -> None:
    """Удаляет пост из БД по ID"""
    try:
        await session.execute(delete(Post).where(Post.id == id))
    except (DisconnectionError, DatabaseError) as err:
        logger.error(err)


async def delete_from_cache():
    """Инвалидация кэша"""
    logger.info('Chache Invalidation')
    await manager.redis.flushdb(asynchronous=True)
    logger.info('Chache cleared')
