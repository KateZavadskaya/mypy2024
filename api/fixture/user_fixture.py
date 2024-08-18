import requests
import pytest
from api.config.settings import (token, baseUrl, postUserUrl,
                                 deleteUserUrl, any_email)


@pytest.fixture()
def obj_id():
    auth_token = token
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Antony",
      "email": any_email,
      "age": 36,
      "phoneNumber": "+12345678901",
      "address": "Spain 123 Main St",
      "role": "user",
      "referralCode": "ABCDEFGH"
    }
    response = requests.post(f"{baseUrl}{postUserUrl}",
                             json=payload,
                             headers=headers,
                             timeout=10)
    response_json = response.json()
    assert 'id' in response_json, "Response JSON does not contain 'id'"
    yield response_json['id']
    requests.delete(f"{baseUrl}{deleteUserUrl}{response_json['id']}",
                    headers=headers,
                    timeout=10)
