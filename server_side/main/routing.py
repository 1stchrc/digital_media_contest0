# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('login/', consumers.UserConsumer.as_asgi()),
]