import uvicorn

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.testclient import TestClient

from views import search_and_delete
from api import posts

app = FastAPI(
    title="FastAPI SearchEngine",
    description="Search information in database using ElasticSearch",
    version="1.0",
    contact={
        "name": "Daniil Sidorenko",
        "email": "sidorenko@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.mount("/static/index.css", StaticFiles(directory="static"), name="static")
test_client = TestClient(app)

app.include_router(posts.router, tags=['api'], prefix='/api')
app.include_router(search_and_delete.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)
