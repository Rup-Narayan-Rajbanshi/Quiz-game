from .base import *
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['rup-game.herokuapp.com']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'davtf4n85sjcri',
        'USER': 'ehgtbainjluitp',
        'HOST': 'ec2-54-158-247-97.compute-1.amazonaws.com',
        'PORT': 5432,
        'PASSWORD':'fbc991a465ae43bc4c8ad77c6d2af8f36d5368916b7305ac13086838754beb31',
    }
}

# # add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500