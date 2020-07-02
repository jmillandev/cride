"""Circles views."""

from rest_framework.generics import ListCreateAPIView
from cride.circles.serializers import CircleSerializer

class ListCreateAPIView(ListCreateAPIView):
    serializer_class = CircleSerializer