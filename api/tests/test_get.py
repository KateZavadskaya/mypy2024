import requests
from jsonschema import validate, ValidationError, SchemaError
from api.fixture.user_fixture import obj_id
from api.config.settings import token, baseUrl, getUserUrl


def test_get_object(obj_id):
    auth_token = token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{baseUrl}{getUserUrl}{obj_id}",
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
        print("JSON-ответ соответствует :) схеме")
    except ValidationError as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)
    except SchemaError as e:
        print("Ошибка в схеме JSON:", e)
