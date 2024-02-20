from rest_framework import serializers
from .models import AppoimentModel
from pets.models import PetModel


class AppoimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppoimentModel
        fields =[
            "pet_id", "veterinarian_id", "date","hour",
            "description", "payed","state","created_at",
         ]
        
class AppoimentCreateSerializer(serializers.Serializer):
    
    pet_id = serializers.IntegerField()
    veterinarian_id = serializers.IntegerField()
    date = serializers.DateField()
    hour = serializers.TimeField()
    description = serializers.CharField()
    payed= serializers.BooleanField(default=False)
    state = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        record = AppoimentModel(**validated_data)
        record.save()
        return record
    
