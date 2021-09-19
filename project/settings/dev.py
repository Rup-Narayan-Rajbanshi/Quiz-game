from .base import *
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['https://rup-game.herokuapp.com/','localhost','127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# # add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500