import jsonschema
import requests
import json_schemas

from utils import load_schema


def test_get_users_status_code_is_ok():
    schema = load_schema('get_users.json')

    response = requests.get(url="https://reqres.in/api/users")

    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
