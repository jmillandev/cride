"""Auth URLs."""

from django.urls import path
from rest_framework_jwt import views

urlpatterns = [
    path('login/', views.obtain_jwt_token),
    path('refresh/', views.refresh_jwt_token),
]