"""
This module contains a test function for creating
 a user object and validating the response.
"""

from venv import logger
import requests
from jsonschema import validate, ValidationError, SchemaError
from api.config.settings import (TOKEN, BASE_URL,
                                 POST_USER_URL, ANY_EMAIL)


def test_create_object():

    """
        Test function to create a user object and validate the response.

        This function sends a POST request to create
         a user object and validates the response status code and JSON schema.
    """

    auth_token = TOKEN
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"}
    payload = {
      "email": ANY_EMAIL,
      "age": 35,
      "phoneNumber": "+12345678901",
      "address": "Poland 123 Main St",
      "role": "user",
      "referralCode": "ABCDQFQQ"
    }
    response = requests.post(f"{BASE_URL}{POST_USER_URL}",
                             json=payload,
                             headers=headers,
                             timeout=10)

    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response.status_code == 200, (f"Ожидался статус-код 200, "
                                         f"но получен {response.status_code}")
    assert response_json.get("name") == payload[
        "name"], (f"Ожидалось имя {payload['name']}, "
                  f"но получено {response_json.get('name')}")
    assert response_json.get("email") == payload[
        "email"], (f"Ожидалось имя {payload['email']}, "
                   f"но получено {response_json.get('email')}")

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "age": {"type": "integer"},
            "phoneNumber": {"type": "string"},
            "address": {"type": "string"},
            "role": {"type": "string"},
            "referralCode": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["id", "name", "email", "age",
                     "phoneNumber", "address", "role",
                     "referralCode", "status"]
    }
    try:
        validate(instance=response_json, schema=schema)
        logger.info("JSON-ответ соответствует :) схеме")
    except ValidationError as e:
        logger.error("JSON-ответ НЕ соответствует :( схеме: %s", e)
    except SchemaError as e:
        logger.error("Ошибка в схеме JSON: %s", e)
