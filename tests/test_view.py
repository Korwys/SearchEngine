import requests


def test_index():
    req = requests.get('http://localhost:8000/')
    assert req.status_code == 200


def test_search():
    req = requests.get('http://localhost:8000/search?q=мерседес')
    value = req.text.find('Всем привет , народ у кого есть мерседес вито')
    assert req.status_code == 200
    assert value != -1


def test_delete():
    req = requests.get('http://localhost:8000/search?q=delete+11')
    value = req.text.find('Объект успешно удален')
    assert value != -1
    assert req.status_code == 200
