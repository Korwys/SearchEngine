##  FASTApi SearchEngine

## О Чем проект:
- Простой поисковик. 
- Реализует поиск информации релевантной запросу пользователя.
- Поиск осуществляется при помощи ElasticSearch. 
- Данных хранятся в Postgres. БД и индексы в ElasticSearch создаются из post.csv.
- При запуске Docker'a,  по адресу http://localhost:8000, будет доступна html страница с input'ом для ввода запроса на получение информации либо удаления объекта по его ID из БД и Elastic'a.
- Реализовано кеширование с помощью Redis. TTL по умолчанию 120 секунд.

## API
### api/search/{you_query}
**Allowed Methods** : GET
<br>**Access Level** : ALL
<br> Возвращает первые 20 документов со всеми полями из БД упорядоченные по дате создания


### /api/delete/id
**Allowed Methods** : DELETE
<br>**Access Level** : ALL
<br>Удаляет документ из индекса и БД по его ID 


## Как запустить
- клонируем репозиторий
- ввести команду docker-compose build -d
- подождать пока все контейнеры стартанут



## Backend
- Framework - FastAPI
- ORM - SQLAlchemy
  - migrations - Alembic
- DB - PostgreSQL
- Search - ElasticSearch
- Cache - Redis
- Template - Jinja2
