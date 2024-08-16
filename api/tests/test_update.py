import requests
import pytest
from jsonschema import validate
from fixture.user_fixture import obj_id
from config.settings import token, baseUrl, updateUserUrl


def test_update_object(obj_id):
    auth_token = token
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Kate",
      "email": "00030@mail.com",
      "age": 35,
      "phoneNumber": "+1234567890",
      "address": "456 Elm Stanciya Zavodskaya",
      "role": "user",
      "referralCode": "AYCDEFGH"

    }
    response = requests.put(f"{baseUrl}{updateUserUrl}{obj_id}",
                            json=payload,
                            headers=headers)
    response_json = response.json()
    print(response.status_code)
    print(response_json)
    # assert response_json["id"] == obj_id, f"заданный {obj_id}, фактич id {response_json['id']} не совпадают"
    assert response_json.get("email") == payload["email"], (f"заданный {payload['email']} "
                                                        f"и фактич {response_json.get("email")} не совпадают")
    assert response_json["age"] == payload["age"], (f"заданный {payload['age']}, "
                                                    f"фактич {response_json['age']} не совпадают")
    assert response_json["address"] == payload["address"], (f"заданный {payload['address']} "
                                                            f"и фактич {response_json['address']} не совпадают")
    assert response_json["phoneNumber"] == payload["phoneNumber"], (f"заданный {payload['phoneNumber']}, "
                                                        f"фактич id {response_json['phoneNumber']} не совпадают")
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
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)
        print("Validation error details:", e)


