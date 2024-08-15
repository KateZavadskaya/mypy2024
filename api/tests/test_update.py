import requests
import pytest
from jsonschema import validate
from fixture.user_fixture import obj_id

token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM3M"
         "jE3NDQsImV4cCI6MTcyMzcyNTM0NH0.4i_1OJVln1CASVqpci1uR5vPZexSZi2ytw-kjVkNW5U")
baseUrl = "https://alexqa.netlify.app/.netlify"
updateUserUrl = "/functions/updateUser/"


def test_update_object(obj_id):
    auth_token = token
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Antonio",
      "email": "157@mail.com",
      "age": 35,
      "address": "Also Spain hgg",
      "phone": "+1234567890"
    }
    response = requests.put(f"{baseUrl}{updateUserUrl}{obj_id}",
                            json=payload,
                            headers=headers)
    response_json = response.json()
    print(response.status_code)
    print(response_json)
    assert response_json["id"] == obj_id, f"заданный {obj_id}, фактич id {response_json['id']} не совпадают"
    assert response_json["email"] == payload["email"], (f"заданный {payload['email']} "
                                                        f"и фактич {response_json['email']} не совпадают")
    assert response_json["age"] == payload["age"], (f"заданный {payload['age']}, "
                                                    f"фактич {response_json['age']} не совпадают")
    assert response_json["address"] == payload["address"], (f"заданный {payload['address']} "
                                                            f"и фактич {response_json['address']} не совпадают")
    assert response_json["phone"] == payload["phone"], (f"заданный {payload['phone']}, "
                                                        f"фактич id {response_json['phone']} не совпадают")
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "age": {"type": "integer"},
            "address": {"type": "string"},
            "phone": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["id", "name", "email", "address", "phone", "status"]
    }
    try:
        validate(instance=response_json, schema=schema)
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)


