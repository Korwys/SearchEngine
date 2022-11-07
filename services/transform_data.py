import pandas as pd

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from sqlalchemy.future import create_engine

from models.db_config import dbname, ip, password, username

elastic_client = Elasticsearch(hosts='https://localhost:9200', basic_auth=('elastic', 'FEAG41B0-rn-aYQqin2g'),
                               ca_certs="../http_ca.crt")


def transform_data_from_file_to_db() -> None:
    """Переносит данные из csv в БД"""
    file = pd.read_csv('../posts.csv')

    df = pd.DataFrame(file, columns=['text', 'created_date', 'rubrics'])
    df_new = df.reindex(columns=['rubrics', 'text', 'created_date'])
    df_new['rubrics'] = df_new['rubrics'].str.replace('[', '{')
    df_new['rubrics'] = df_new['rubrics'].str.replace(']', '}')

    db = create_engine(f"postgresql://{username}:{password}@{ip}/{dbname}")
    df_new.to_sql('posts', db, if_exists='append', index=False, )


def add_data_to_elastic() -> dict:
    """Добавляет данные из csv в индекс ElasticSearch"""
    df = pd.read_csv('../posts.csv', usecols=[0])
    for index, value in enumerate(df.to_dict(orient="records")):
        yield {
            "_index": "posts6",
            "id": f"{index + 1}",
            "text": value['text']
        }


def main():
    transform_data_from_file_to_db()
    elastic_client.indices.create(index='posts6')
    bulk(elastic_client, add_data_to_elastic())


if __name__ == '__main__':
    main()
