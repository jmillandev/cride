from django.urls import path

from cride.circles.views import ListCreateAPIView

urlpatterns = [
    path('', ListCreateAPIView.as_view())
]