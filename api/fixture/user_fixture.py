import requests
import pytest


token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM3M"
         "jE3NDQsImV4cCI6MTcyMzcyNTM0NH0.4i_1OJVln1CASVqpci1uR5vPZexSZi2ytw-kjVkNW5U")
baseUrl = "https://alexqa.netlify.app/.netlify"
postUserUrl = "/functions/createUser"
deleteUserUrl = "/functions/deleteUser/"


@pytest.fixture()
def obj_id():
    auth_token = token
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Antony",
      "email": "179@mail.com",
      "age": 36,
      "address": "Spain"
    }
    response = requests.post(f"{baseUrl}{postUserUrl}",
                             json=payload,
                             headers=headers).json()
    yield response.get("id")
    requests.delete(f"{baseUrl}{deleteUserUrl}{response.get("id")}",
                    headers=headers)
