from .base import *
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['rup-game-realtime.herokuapp.com']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfg7cflmaov4g0',
        'USER': 'iwnkxrlqaguocz',
        'HOST': 'ec2-34-228-154-153.compute-1.amazonaws.com',
        'PORT': 5432,
        'PASSWORD':'d21e23d60a341d4104e8e128adbe284e8c33a643aee4ff4d14d8e75d53115e10',
    }
}

# # add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500