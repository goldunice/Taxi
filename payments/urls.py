from django.urls import path
from .views import *
urlpatterns = [
    path('all_payment/', AllPaymentAPIView.as_view()),
    path('payment/<int:pk>/', PaymentAPIView.as_view()),
]
