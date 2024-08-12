import requests
from jsonschema import validate


baseURL = "https://alexqa.netlify.app/.netlify"
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM0MDkyMDgsImV4cCI6MTcyMzQxMjgwOH0.aQHp8dFWxGdw_qtOCmwCMRsLyuNQq5H__-ZyQzYUfhA"
id_N = "66b9264ea3cdd306e6c58f8e"

# GET_getUser
endpoint = "/functions/getUser/"
headers = {"Authorization": f"Bearer {auth_token}"}
response = requests.get(f"{baseURL}{endpoint}{id_N}", headers=headers)
print(response.status_code)
assert response.status_code == 200, f"Does not get UserInfo, status code is {response.status_code}"
print(response.json())
json_response = response.json()

schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"},
        "createdBy": {"type": "integer"}
    },
    "required": ["_id", "name", "email", "createdAt", "createdBy"]
}
try:
    validate(instance=json_response, schema=schema)
    print("JSON-ответ соответствует схеме")
except Exception as e:
    print("JSON-ответ НЕ соответствует схеме:", e)




