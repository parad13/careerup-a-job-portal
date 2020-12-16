import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = (os.environ.get('DEBUG_VALUE') == True)
pass1 = os.environ.get('DATABASE_PASS')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

print(SECRET_KEY,DEBUG,pass1,EMAIL_HOST_PASSWORD)
