
import requests
from jsonschema import validate
from fixture.user_fixture import obj_id
from config.settings import token, baseUrl, getUserUrl


def test_get_object(obj_id):
    auth_token = token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{baseUrl}{getUserUrl}{obj_id}",
                            headers=headers)
    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert response_json["_id"] == obj_id, f"заданный {obj_id}, фактич id {response_json["_id"]} не совпадают"
    schema = {
        "type": "object",
        "properties": {
            "_id": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "createdAt": {"type": "string", "format": "date-time"},
            "createdBy": {"type": "integer"}
        },
        "required": ["_id", "name", "createdAt", "createdBy"]
    }
    try:
        validate(instance=response_json, schema=schema)
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)
        print("Validation error details:", e)
