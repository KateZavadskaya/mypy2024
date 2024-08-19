"""
This module contains a test function for deleting
 a user object and validating the response.
"""

import requests
from api.fixture.user_fixture import obj_id
from api.config.settings import (TOKEN, BASE_URL,
                                 DELETE_USER_URL)


def test_delete_object(obj_id):

    """
        Test function to delete a user object and validate the response.

        This function sends a DELETE request to remove
        a user object and validates
        the response status code. It also checks the status
        code for a repeated delete request.
        """

    auth_token = TOKEN
    headers = {"Authorization": f"Bearer {auth_token}"}
    response_del = requests.delete(f"{BASE_URL}{DELETE_USER_URL}{obj_id}",
                                   headers=headers,
                                   timeout=10)
    response_json_del = response_del.json()
    print(response_json_del)
    assert response_del.status_code == 404, \
        f"Удаление не прошло, итоговый статус код {response_del.status_code}"
    response_del2 = requests.delete(f"{BASE_URL}{DELETE_USER_URL}{obj_id}",
                                    headers=headers,
                                    timeout=10)
    response_json_del2 = response_del2.json()
    print(response_json_del2)
    assert response_del2.status_code == 404, \
        (f"Проверка повторного удаления не прошла, "
         f"итоговый статус код {response_del2.status_code}")
