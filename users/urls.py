from django.urls import path
from .views import *
urlpatterns = [
    path('driver_token/', DriverTokenAPIView.as_view()),
    path('operator_token/', OperatorTokenAPIView.as_view()),
]
