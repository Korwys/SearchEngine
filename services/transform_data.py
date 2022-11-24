import logging

import pandas as pd

from elasticsearch.helpers import bulk
from sqlalchemy.future import create_engine

from config.env_config import settings
from config.setup_manager import manager

logger = logging.getLogger('app.services.transform_data')


def transform_data_from_file_to_db() -> None:
    """Переносит данные из csv в БД"""
    file = pd.read_csv('../posts.csv')

    df = pd.DataFrame(file, columns=['text', 'created_date', 'rubrics'])
    df_new = df.reindex(columns=['rubrics', 'text', 'created_date'])
    df_new['rubrics'] = df_new['rubrics'].str.replace('[', '{')
    df_new['rubrics'] = df_new['rubrics'].str.replace(']', '}')

    db = create_engine(
        f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_address}/{settings.db_name}")
    df_new.to_sql('posts', db, if_exists='append', index=False, )


def add_data_to_elastic() -> dict:
    """Добавляет данные из csv в индекс ElasticSearch"""
    df = pd.read_csv('../posts.csv', usecols=[0])
    for index, value in enumerate(df.to_dict(orient="records")):
        yield {
            "_index": "posts",
            "id": f"{index + 1}",
            "text": value['text']
        }


def main() -> None:
    try:
        transform_data_from_file_to_db()
        if manager.elastic_server.indices.exists(index='posts'):
            manager.elastic_server.indices.delete(index='posts')
        manager.elastic_server.indices.create(index='posts')
        bulk(manager.elastic_server, add_data_to_elastic())
    except Exception as err:
        logger.exception(err)


if __name__ == '__main__':
    main()
