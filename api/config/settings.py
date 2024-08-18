import random
token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2V"
         "ySWQiOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQ"
         "iOjE3MjQwMDkxMTEsImV4cCI6MTcyNDAxMjcxMX0.oX3"
         "T64J57jTWAwFmAq2Ic5lw4fy4ve7_Kje1LHon1H0")
baseUrl = "https://alexqa.netlify.app/.netlify"
postUserUrl = "/functions/createUser"
getUserUrl = "/functions/getUser/"
deleteUserUrl = "/functions/deleteUser/"
updateUserUrl = "/functions/updateUser/"

# for random mail
random_number = random.randint(1000, 9999)
any_email = f"1230028_{random_number}@mail.com"
any_email_update = f"1230028_{random_number}@mail.com"
