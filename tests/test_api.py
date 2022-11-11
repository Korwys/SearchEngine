import requests


def test_apiget():
    req = requests.get('http://localhost:8000/api/search/привет')
    response = req.json()
    assert response[0]['rubrics'] == ["'VK-1603736028819866'", "'VK-12226415716'", "'VK-38169460183'"]
    assert req.status_code == 200


def test_api_delete():
    req = requests.delete('http://localhost:8000/api/delete/{post_id}?id=41')
    response = req.json()
    assert response['message'] == 'Object deleted'
    assert req.status_code == 200
