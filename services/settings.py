import redis
from elasticsearch import Elasticsearch, AsyncElasticsearch


class SettingManager:
    redis = redis.Redis(host='cache', port=6379, db=0)

    elastic_server = Elasticsearch(hosts='http://es03:9200')

    async_elastic_client = AsyncElasticsearch(hosts='http://es01:9200')


manager = SettingManager()
