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
            'password': '1234',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Paulo',
        'email': 'prmorais1302@gmail.com',
        'id': 1,
    }


def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Paulo',
                'email': 'prmorais1302@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Paulo Roberto',
            'email': 'prmorais1302@gmail.com',
            'password': '1234',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Paulo Roberto',
        'email': 'prmorais1302@gmail.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
