from rest_framework import serializers
from .models import PetModel


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = '__all__'