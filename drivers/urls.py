from django.urls import path
from .views import *

urlpatterns = [
    path('all_category/', AllCarCategoryAPIView.as_view()),
    path('all_driver/', AllDriverAPIView.as_view()),
    path('category/<int:pk>/', CarCategoryAPIView.as_view()),
    path('driver/<int:pk>/', DriverAPIView.as_view()),
]
