import redis
from elasticsearch import Elasticsearch, AsyncElasticsearch


class SettingManager:
    redis = redis.Redis(host='cache', port=6379, db=0, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')

    elastic_server = Elasticsearch(hosts='http://es03:9200')

    async_elastic_client = AsyncElasticsearch(hosts='http://es02:9200')


manager = SettingManager()
