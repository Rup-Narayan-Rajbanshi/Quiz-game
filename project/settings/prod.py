
from .base import *
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['rup-game.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        # 'ROUTING': 'project.routing.channel_routing',
    }
}


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'HOST': os.environ.get('HOST'),
        'PORT': 5432,
        'PASSWORD':os.environ.get('DATABASE_PASSWORD'),
    }
}


STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"staticfiles")
STATIC_URL = '/static/'
