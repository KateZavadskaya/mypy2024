"""
This module contains a pytest fixture for creating and deleting a user object.
"""

import requests
import pytest
from api.config.settings import (TOKEN, BASE_URL, POST_USER_URL,
                                 DELETE_USER_URL, ANY_EMAIL)


@pytest.fixture
def obj_id():
    """
    Fixture to create a user object and return its ID.
    The user object is deleted after the test is done.
    """

    auth_token = TOKEN
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"}
    payload = {
      "name": "Antony",
      "email": ANY_EMAIL,
      "age": 36,
      "phoneNumber": "+12345678901",
      "address": "Spain 123 Main St",
      "role": "user",
      "referralCode": "ABCDEFGH"
    }
    response = requests.post(f"{BASE_URL}{POST_USER_URL}",
                             json=payload,
                             headers=headers,
                             timeout=10)
    response_json = response.json()
    assert 'id' in response_json, "Response JSON does not contain 'id'"
    yield response_json['id']
    requests.delete(f"{BASE_URL}{DELETE_USER_URL}{response_json['id']}",
                    headers=headers,
                    timeout=10)
