import json

from redis.exceptions import ConnectionError

from config.setup_manager import manager


def redis_cache(data: list, query: str) -> list:
    try:
        response = [{"text": i.text, "id": i.id, "created_date": i.created_date, "rubrics": i.rubrics} for i in data]
        redis_data = json.dumps(response, default=str)
        manager.redis.set(query, redis_data, ex=120)
        return response
    except ConnectionError as e:
        print(e)