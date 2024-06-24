from http import HTTPStatus

from fast_api_zero.schemas import UserPublic


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
    assert response.json() == {'users': []}


# teste buscando todos os usuários usando user
def test_get_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


# teste buscando um usuário com sucesso
def test_get_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


# teste atualizando um usuário com sucesso
def test_update_user(client, user):
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
def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': f'User {user.id} deleted'}


# teste removendo um usuário inexistente e exibindo erro
def test_delete_user_not_found(client):
    response = client.delete('/users/5')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User with id 5 not found!'}
