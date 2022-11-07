from fastapi import Depends
from api.posts import delete_id
from main import test_client
from models.db_config import get_db

session = Depends(get_db)


fake_db={
    1:{'id':1, "text": 'привет', 'rubrics':['asd','mmm','ppp'], 'created_date': 10-12-2021},
    2:{'id':2, "text": 'привет-пока', 'rubrics':['ooo','fff','ppp'], 'created_date': 10-12-2021},
    3:{'id':3, "text": 'пока', 'rubrics':['asd','fff','ppp'], 'created_date': 10-13-2021},
    4:{'id':4, "text": 'как дела?', 'rubrics':['vvv','fff','ppp'], 'created_date': 10-13-2021},
    5:{'id':5, "text": 'ты кто?', 'rubrics':['www','fff','ppp'], 'created_date': 10-14-2021}
}


def test_main():
    response = test_client.get('/')
    assert response.status_code == 200

def test_search():
    response = test_client.get('/search?q=привет')
    assert response.status_code == 200


#
# def test_search():
#     assert await delete_id(10, session=session) == {"message": "Object deleted"}

