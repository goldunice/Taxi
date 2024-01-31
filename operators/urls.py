from django.urls import path
from .views import *

urlpatterns = [
    path('all_operator/', AllOperatorAPIView.as_view()),
    path('operator/<int:pk>/', OperatorAPIView.as_view()),
    path('all_client/', AllClientAPIView.as_view()),
    path('client/<int:pk>/', ClientAPIView.as_view()),
    path('all_order/', AllOrderAPIView.as_view()),
    path('order/<int:pk>/', OrderAPIView.as_view()),
]
