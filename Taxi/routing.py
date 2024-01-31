from django.urls import path
from operators.consumers import *


websocket_urlpatterns = [
    path('ws/all_order/', OrderConsumer.as_asgi())
]