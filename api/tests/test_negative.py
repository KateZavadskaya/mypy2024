import requests
from jsonschema import validate
import pytest
from fixture.user_fixture import obj_id
from config.settings import token, baseUrl, postUserUrl


def test_create_object():
    auth_token = token
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Vita",
      "email": "000007@mail.com",
      "age": 35,
      "phoneNumber": "+12345678901",
      "address": "Poland 123 Main St",
      "role": "user",
      "referralCode": "ABCDQFQQ"
    }
    response = requests.post(f"{baseUrl}{postUserUrl}",
                             json=payload,
                             headers=headers)

    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert response_json.get("name") == payload[
        "name"], f"Ожидалось имя {payload['name']}, но получено {response_json.get('name')}"
    assert response_json.get("email") == payload[
        "email"], f"Ожидалось имя {payload['email']}, но получено {response_json.get('email')}"

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
        "required": ["id", "name", "email", "age", "phoneNumber", "address", "role",
                     "referralCode", "status"]
    }
    try:
        validate(instance=response_json, schema=schema)
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)



