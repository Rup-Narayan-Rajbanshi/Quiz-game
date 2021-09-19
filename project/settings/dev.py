from .base import *
# from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['https://rup-game.herokuapp.com/','localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}