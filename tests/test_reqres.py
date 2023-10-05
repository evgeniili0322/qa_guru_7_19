import jsonschema
import requests

from utils import load_schema


base_url = 'https://reqres.in'


def test_get_users_status_code_is_ok():
    response = requests.get(url=f'{base_url}/api/users')

    assert response.status_code == 200


def test_get_users_schema_validation():
    schema = load_schema('get_users.json')

    response = requests.get(url=f'{base_url}/api/users')

    jsonschema.validate(response.json(), schema)


def test_get_single_user_status_code_is_ok():
    response = requests.get(url=f'{base_url}/api/users/2')

    assert response.status_code == 200


def test_get_single_user_schema_validation():
    schema = load_schema('get_single_user.json')

    response = requests.get(url=f'{base_url}/api/users/2')

    jsonschema.validate(response.json(), schema)


def test_post_users_status_code_is_ok():
    response = requests.post(
        url=f'{base_url}/api/users',
        json={
            'name': "morpheus",
            'job': 'leader'
        }
    )

    assert response.status_code == 201


def test_post_users_schema_validation():
    schema = load_schema('post_users.json')

    response = requests.post(
        url=f'{base_url}/api/users',
        json={
            'name': 'morpheus',
            'job': 'leader'
        }
    )

    jsonschema.validate(response.json(), schema)


def test_post_users_response_body_data():
    response = requests.post(
        url=f'{base_url}/api/users',
        json={
            'name': 'morpheus',
            'job': 'leader'
        }
    )

    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'


def test_put_users_status_code_is_ok():
    response = requests.put(
        url=f'{base_url}/api/users/2',
        json={
            'name': 'morpheus',
            'job': 'resident'
        }
    )

    assert response.status_code == 200


def test_put_users_schema_validation():
    schema = load_schema('put_users.json')

    response = requests.put(
        url=f'{base_url}/api/users/2',
        json={
            'name': 'morpheus',
            'job': 'resident'
        }
    )

    jsonschema.validate(response.json(), schema)


def test_put_users_response_body_data():
    response = requests.put(
        url=f'{base_url}/api/users/2',
        json={
            'name': 'morpheus',
            'job': 'resident'
        }
    )

    assert response.json()['job'] == 'resident'
