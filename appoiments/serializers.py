from rest_framework import serializers
from .models import AppoimentModel
from pets.models import PetModel
from django.shortcuts import get_object_or_404


class AppoimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppoimentModel
        fields =[
            "id",
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
    
class AppoimentUpdateSerializer(serializers.Serializer):
    #pet_id = serializers.IntegerField()
    #veterinarian_id = serializers.IntegerField()
    date = serializers.DateField()
    hour = serializers.TimeField()
    description = serializers.CharField()
    payed= serializers.BooleanField(default=False)
    state = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        #print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class AppoimentDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def deactivate(self):
        appoiment_id = self.validated_data['id']
        record = get_object_or_404(AppoimentModel, pk=appoiment_id, is_delete=False)
        record.is_delete=True
        record.save()