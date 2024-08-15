import requests
from jsonschema import validate

token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM3M"
         "jE3NDQsImV4cCI6MTcyMzcyNTM0NH0.4i_1OJVln1CASVqpci1uR5vPZexSZi2ytw-kjVkNW5U")
baseUrl = "https://alexqa.netlify.app/.netlify"
postUserUrl = "/functions/createUser"


def test_create_object():
    auth_token = token
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Antony",
      "email": "303@mail.com",
      "age": 36,
      "address": "SpainSpainSpainSpain"
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
            "status": {"type": "string"}
        },
        "required": ["id", "name", "email", "status"]
    }
    try:
        validate(instance=response_json, schema=schema)
        print("JSON-ответ соответствует :) схеме")
    except Exception as e:
        print("JSON-ответ НЕ соответствует :( схеме:", e)
