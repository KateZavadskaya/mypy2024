"""Constants for api-project"""

import random
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2V"
         "ySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQ"
         "iOjE3MjQwNjcwMjQsImV4cCI6MTcyNDA3MDYyNH0.uLw"
         "QsUIW2SxrY5r8iLCU9Tp6q0SF6PNMtKe6vnsk94k")
BASE_URL = "https://alexqa.netlify.app/.netlify"
POST_USER_URL = "/functions/createUser"
GET_USER_URL = "/functions/getUser/"
DELETE_USER_URL = "/functions/deleteUser/"
UPDATE_USER_URL = "/functions/updateUser/"

# for random mail
RANDOM_NUMBER = random.randint(1000, 9999)
ANY_EMAIL = f"1230028_{RANDOM_NUMBER}@mail.com"
ANY_EMAIL_UPDATE = f"1230028_{RANDOM_NUMBER}@mail.com"
ANY_EMAIL_CREATE = f"1230028_{RANDOM_NUMBER}@mail.com"
