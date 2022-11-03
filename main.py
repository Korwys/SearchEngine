from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch

app = FastAPI()
elastic = AsyncElasticsearch()

@app.on_event("shutdown")
async def app_shutdown():
    await elastic.close()


