import jsonschema
import allure
import json

from utils import load_schema
from requests import sessions
from curlify import to_curl
from allure_commons.types import AttachmentType


def reqres_api(method, base_url, url, **kwargs):
    current_base_url = {
        'reqres': 'https://reqres.in',
        'catfact': 'https://catfact.ninja'
                        }
    new_url = current_base_url[base_url] + url

    with allure.step(f'{method.upper()} {url}'):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            response_json = json.dumps(response.json(), indent=4).encode('utf8')

            allure.attach(body=message.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            allure.attach(body=response_json, name='Response Json',
                          attachment_type=AttachmentType.JSON, extension='json')
    return response


def test_get_users_status_code_is_ok():
    response = reqres_api(
        'get',
        base_url='reqres',
        url='/api/users'
    )

    assert response.status_code == 200


def test_get_users_schema_validation():
    schema = load_schema('get_users.json')

    response = reqres_api(
        'get',
        base_url='reqres',
        url='/api/users'
    )

    jsonschema.validate(response.json(), schema)


def test_get_single_user_status_code_is_ok():
    response = reqres_api(
        'get',
        base_url='reqres',
        url='/api/users/2'
    )

    assert response.status_code == 200


def test_get_single_user_schema_validation():
    schema = load_schema('get_single_user.json')

    response = reqres_api(
        'get',
        base_url='reqres',
        url='/api/users/2'
    )

    jsonschema.validate(response.json(), schema)


def test_post_users_status_code_is_ok():
    response = reqres_api(
        'post',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'leader'
        }
    )

    assert response.status_code == 201


def test_post_users_schema_validation():
    schema = load_schema('post_users.json')

    response = reqres_api(
        'post',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'leader'
        }
    )

    jsonschema.validate(response.json(), schema)


def test_post_users_response_body_data():
    response = reqres_api(
        'post',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'leader'
        }
    )

    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'


def test_put_users_status_code_is_ok():
    response = reqres_api(
        'put',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'resident'
        }
    )

    assert response.status_code == 200


def test_put_users_schema_validation():
    schema = load_schema('put_users.json')

    response = reqres_api(
        'put',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'resident'
        }
    )

    jsonschema.validate(response.json(), schema)


def test_put_users_response_body_data():
    response = reqres_api(
        'put',
        base_url='reqres',
        url='/api/users/2',
        json={
            'name': "morpheus",
            'job': 'resident'
        }
    )

    assert response.json()['job'] == 'resident'
