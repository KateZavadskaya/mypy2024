"""
This module contains a test function for updating
a user object and validating the response.
"""

from venv import logger
import requests
from jsonschema import validate, ValidationError, SchemaError
from api.config.settings import (TOKEN, BASE_URL,
                                 UPDATE_USER_URL, ANY_EMAIL_UPDATE)


def test_update_object(obj_id):
    """
        Test function to update a user object and validate the response.

        This function sends a PUT request to update
        a user object and validates the response status code and JSON schema.
"""

    auth_token = TOKEN
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Kate",
      "email": ANY_EMAIL_UPDATE,
      "age": 35,
      "phoneNumber": "+1234567890",
      "address": "456 Elm Stanciya Zavodskaya",
      "role": "user",
      "referralCode": "AYCDEFGH"

    }
    response = requests.put(f"{BASE_URL}{UPDATE_USER_URL}{obj_id}",
                            json=payload,
                            headers=headers,
                            timeout=10)
    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response_json["id"] == obj_id, \
        f"заданный {obj_id}, фактич id {response_json['id']} не совпадают"
    assert response_json.get("email") == payload["email"], \
        (f"заданный {payload['email']} "
         f"и фактич {response_json.get('email')} не совпадают")
    assert response_json["age"] == payload["age"], \
        (f"заданный {payload['age']}, и фактич {response_json['age']} "
         f"не совпадают")
    assert response_json["address"] == payload["address"], \
        (f"заданный {payload['address']} и фактич {response_json['address']} "
         f"не совпадают")
    assert response_json["phoneNumber"] == payload["phoneNumber"], \
        (f"заданный {payload['phoneNumber']}, "
         f"фактич {response_json['phoneNumber']} не совпадают")
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
        "required": ["id", "name", "email", "age", "phoneNumber",
                     "address", "role", "referralCode", "status"]
    }
    try:
        validate(instance=response_json, schema=schema)
        logger.info("JSON-ответ соответствует :) схеме")
    except ValidationError as e:
        logger.error("JSON-ответ НЕ соответствует :( схеме: %s", e)
    except SchemaError as e:
        logger.error("Ошибка в схеме JSON: %s", e)
