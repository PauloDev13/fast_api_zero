from http import HTTPStatus

# from fastapi.testclient import TestClient
#
# from fast_api_zero.app import app
#
# client = TestClient(app)


def test_root_dev_retornar_ok_e_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Paulo',
            'email': 'prmorais1302@gmail.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Paulo',
        'email': 'prmorais1302@gmail.com',
        'id': 1,
    }
