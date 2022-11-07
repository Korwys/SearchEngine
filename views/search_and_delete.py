from fastapi import Depends, Request, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates, _TemplateResponse

from models.db_config import get_db
from services.crud import delete_id_in_elastic, delete_id_in_db, get_search_results_by_text

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse)
async def get_results(request: Request)-> _TemplateResponse:
    """Возвращает главную страницу"""
    return templates.TemplateResponse("index.html", {"request": request})


@router.get('/search', response_class=HTMLResponse)
async def get_results(request: Request, session: AsyncSession = Depends(get_db))-> _TemplateResponse:
    """Возвращает списсок результатов поиска или ответ при удалении объекта по ID"""
    query = request.query_params['q']
    if 'delete' in query:
        data = int(query.split()[1])
        await delete_id_in_elastic(id=data)
        await delete_id_in_db(id=data, session=session)
        return templates.TemplateResponse("index.html",
                                          {"request": request, "response": [{"text": "Объект успешно удален"}]})
    else:
        response = await get_search_results_by_text(data=query, session=session)
        return templates.TemplateResponse("index.html", {"request": request, "response": response})