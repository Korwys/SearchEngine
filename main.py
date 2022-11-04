from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch

from api import posts

app = FastAPI(
    title="FastAPI SearchEngine",
    description="Seach information in database using ElasticSearch",
    version="1.0",
    contact={
        "name": "Daniil Sidorenko",
        "email": "sidorenko@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)



app.include_router(posts.router,tags=['posts'], prefix='/posts')
