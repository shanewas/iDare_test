from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/status/', WSConsumer.as_asgi())
]