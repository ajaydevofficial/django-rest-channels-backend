"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing as chat_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    """
        ProtocolTypeRouter checks the type of requests incoming, if it is an http request then we use the normal 
        get_asgi_application function to handle it. Else we will use consumers
    """
    "http": get_asgi_application(),
    "websocket":
        URLRouter(
            chat_routing.websocket_urlpatterns
        )
})

