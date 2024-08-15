import requests
from jsonschema import validate
from fixture.user_fixture import obj_id

token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM3M"
         "jE3NDQsImV4cCI6MTcyMzcyNTM0NH0.4i_1OJVln1CASVqpci1uR5vPZexSZi2ytw-kjVkNW5U")
baseUrl = "https://alexqa.netlify.app/.netlify"
deleteUserUrl = "/functions/deleteUser/"


def test_delete_object(obj_id):
    auth_token = token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response_del = requests.delete(f"{baseUrl}{deleteUserUrl}{obj_id}", headers=headers)
    response_json_del = response_del.json()
    print(response_json_del)
    assert response_del.status_code == 200, f"Первое удаление, фактический статус код {response_del.status_code}"
    response_del2 = requests.delete(f"{baseUrl}{deleteUserUrl}{obj_id}", headers=headers)
    response_json_del2 = response_del2.json()
    print(response_json_del2)
    assert response_del2.status_code == 404, f"Второе удаление, фактический статус код {response_del2.status_code}"
