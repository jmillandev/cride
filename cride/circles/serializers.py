"""Circle serializers"""

from rest_framework import serializers

from cride.circles.models import Circle

class CircleSerializer(serializers.ModelSerializer):
    """Circle Serializer"""
    
    class Meta:
        model = Circle
        fields = '__all__'