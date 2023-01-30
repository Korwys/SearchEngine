import json
import logging

from redis.exceptions import ConnectionError

from src.config.setup_manager import manager

logger = logging.getLogger('app.services.redis_cache')


def redis_cache(data: list, query: str) -> list:
    try:
        response = [{"text": i.text, "id": i.id, "created_date": i.created_date, "rubrics": i.rubrics} for i in data]
        redis_data = json.dumps(response, default=str)
        manager.redis.set(query, redis_data, ex=120)
        return response
    except ConnectionError as err:
        logger.error(err)
