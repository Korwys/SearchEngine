import redis

from pydantic import BaseSettings
from elasticsearch import Elasticsearch, AsyncElasticsearch

class AppConfig(BaseSettings):
    db_username: str
    db_password: str
    db_address: str
    db_name: str

    class Config:
        env_file = '../.env'


settings = AppConfig()



class SettingManager:
    redis = redis.Redis(host='cache', port=6379, db=0)

    elastic_server = Elasticsearch(hosts='http://es03:9200')

    async_elastic_client = AsyncElasticsearch(hosts='http://es01:9200')


manager = SettingManager()
