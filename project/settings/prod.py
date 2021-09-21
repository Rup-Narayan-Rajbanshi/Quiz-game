
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
        'NAME': 'davtf4n85sjcri',
        'USER': 'ehgtbainjluitp',
        'HOST': 'ec2-54-158-247-97.compute-1.amazonaws.com',
        'PORT': 5432,
        'PASSWORD':'fbc991a465ae43bc4c8ad77c6d2af8f36d5368916b7305ac13086838754beb31',
    }
}


STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"staticfiles")
STATIC_URL = '/static/'
