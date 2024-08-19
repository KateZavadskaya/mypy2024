"""
This module contains a test function for retrieving
a user object and validating the response.
"""

from venv import logger
import requests
from jsonschema import (validate,
                        ValidationError, SchemaError)
from api.config.settings import TOKEN, BASE_URL, GET_USER_URL


def test_get_object(obj_id):
    """
        Test function to retrieve a user object and validate the response.

        This function sends a GET request to retrieve
        a user object and validates the response status code and JSON schema.
    """

    auth_token = TOKEN
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}{GET_USER_URL}{obj_id}",
                            headers=headers,
                            timeout=10)
    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response.status_code == 200, \
        f"Ожидался статус-код 200, но получен {response.status_code}"
    assert response_json["id"] == obj_id, \
        f"заданный {obj_id}, фактич id {response_json['id']} не совпадают"
    schema = {
        "type": "object",
        "properties": {
            "d": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "age": {"type": "integer"},
            "phoneNumber": {"type": "string"},
            "address": {"type": "string"},
            "role": {"type": "string"},
            "referralCode": {"type": "string"},
            "createdAt": {"type": "string",
                          "format": "date-time"},
            "createdBy": {"type": "string"}
        },
        "required": ["id", "name", "age", "phoneNumber",
                     "address", "role", "referralCode",
                     "createdAt", "createdBy"]
    }
    try:
        validate(instance=response_json, schema=schema)
        logger.info("JSON-ответ соответствует :) схеме")
    except ValidationError as e:
        logger.error("JSON-ответ НЕ соответствует :( схеме: %s", e)
    except SchemaError as e:
        logger.error("Ошибка в схеме JSON: %s", e)
