import requests
import pytest
from jsonschema import validate
from config.settings import token, baseUrl, postUserUrl, deleteUserUrl


@pytest.fixture()
def obj_id():
    auth_token = token
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"}
    payload = {
        "name": "NinaFix",
        "email": "181@mail.com",
        "age": 35,
        "phoneNumber": "+12345678901",
        "address": "Spain 123 Main St",
        "role": "user",
        "referralCode": "BODWEFQQ"
    }
    response = requests.post(f"{baseUrl}{postUserUrl}",
                             json=payload,
                             headers=headers)

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
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)
    response_json = response.json()
    assert 'id' in response_json, "Response JSON does not contain 'id'"
    print(response_json['id'])
    yield response_json['id']
    requests.delete(f"{baseUrl}{deleteUserUrl}{response_json['id']}",
                    headers=headers)
