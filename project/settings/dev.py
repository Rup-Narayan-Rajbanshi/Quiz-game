from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}