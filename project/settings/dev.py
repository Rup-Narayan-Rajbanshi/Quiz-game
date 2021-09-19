from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['https://rup-game.herokuapp.com/','localhost']


DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}