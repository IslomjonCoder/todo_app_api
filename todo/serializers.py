from rest_framework import serializers
from .models import Todo, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    # status = StatusSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
