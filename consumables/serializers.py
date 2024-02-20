from rest_framework import serializers
from .models import GameConsumable

class GameConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameConsumable
        fields = '__all__'