"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path

from trivia_game.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.prod')

ws_patterns = [
    path('ws/new/',NewConsumers.as_asgi())
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ws_patterns
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})
