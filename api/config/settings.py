"""Constants for api-project"""

import random
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1"
         "c2VySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiL"
         "CJpYXQiOjE3MjQxMDIxMjAsImV4cCI6MTcyNDEwNT"
         "cyMH0.TZw8G-mYq9ViiHCGOXlT8WOy1krAVv3B-Up"
         "zCrkxzLU")
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
