import json

from services.settings import manager


def redis_cache(data: list, query: str) -> list:
    response = [{"text": i.text, "id": i.id, "created_date": i.created_date, "rubrics": i.rubrics} for i in data]
    redis_data = json.dumps(data, default=str)
    manager.redis.set(query, redis_data, ex=120)
    return response
