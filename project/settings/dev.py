from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = config('SECRET_KEY')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        },
        # 'ROUTING': 'project.routing.channel_routing',
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn")

MEDIA_URL= '/media_cdn/'
 
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"media_cdn")
