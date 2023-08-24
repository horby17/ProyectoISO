import os

from django.db import connection
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL ={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventarios',
        'USER': 'root',
        'PASSWORD': 'horby17',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}
