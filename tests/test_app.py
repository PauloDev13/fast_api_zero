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


# teste criando um usuário
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


# teste buscando todos os usuários
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


# teste buscando um usuário com sucesso
def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Paulo',
        'email': 'prmorais1302@gmail.com',
        'id': 1,
    }


# teste atualizando um usuário com sucesso
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


# teste atualizando um usuário inexistente e exibindo erro
def test_update_user_not_found(client):
    response = client.put(
        '/users/10',
        json={
            'username': 'Paulo Roberto',
            'email': 'prmorais1302@gmail.com',
            'password': '1234',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User with id 10 not found!'}


# teste removendo um usuário com sucesso
def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


# teste removendo um usuário inexistente e exibindo erro
def test_delete_user_not_found(client):
    response = client.delete('/users/5')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User with id 5 not found!'}
