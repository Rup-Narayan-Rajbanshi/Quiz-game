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
        'NAME': 'd5jtvnmjaesr1q',
        'USER': 'mvlalvzyzqnyrd',
        'HOST': 'ec2-18-214-238-28.compute-1.amazonaws.com',
        'PORT': 5432,
        'PASSWORD':'d13184981df7ff2462e5829009af1b41ccc781e121b57ebb95b522825f4cd623',
    }
}

# # add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500