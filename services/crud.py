from elasticsearch import AsyncElasticsearch
from elasticsearch import exceptions as Exp
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc
from sqlalchemy.future import select

from models.posts import Post


elastic_client = AsyncElasticsearch(hosts='https://localhost:9200', basic_auth=('elastic', 'FEAG41B0-rn-aYQqin2g'),
                                    ca_certs="http_ca.crt")


async def get_search_results_by_text(data: str, session: AsyncSession):
    """Возвращает результы поискового запроса"""
    try:
        elastic_query = await elastic_client.search(
            index="posts6",
            query={"match": {"text": data}},
            size=10000
        )
        list_id = [item['_source']['id'] for item in elastic_query['hits']['hits']]
        new_query = list(map(int, list_id))
        result = await session.execute(
            select(Post).where(Post.id.in_(new_query)).order_by(Post.created_date.desc()).limit(20))
        return result.scalars().all()
    except (Exp.NotFoundError, Exp.ConnectionError) as e:
        print(e)


async def delete_id_in_elastic(id: int) -> None:
    """Удаляет документы из elastica по ID"""
    try:
        fetch_element_by_id = await elastic_client.search(index='posts', query={"match": {"id": id}})
        elastic_id = fetch_element_by_id['hits']['hits'][0]['_id']
        await elastic_client.delete(index='nole3', id=elastic_id)
    except (Exp.NotFoundError, Exp.ConnectionError) as e:
        print(e)


async def delete_id_in_db(id: int, session: AsyncSession) -> None:
    """Удаляет пост из БД по ID"""
    try:
        await session.execute(delete(Post).where(Post.id == id))
    except (ValueError, TypeError, exc.NoResultFound, exc.DatabaseError) as e:
        print(e)
