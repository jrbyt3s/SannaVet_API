from rest_framework import serializers
from django.shortcuts import get_list_or_404
from .models import AttentionModel
from datetime import datetime

class AttentionSerializer(serializers.Serializer):
    class Meta:
        model =AttentionModel
        fields = [
            "id","pet_id", "diagnosis", "treatment",
            "procedure", "imageUrl","dateOfAttention",
        ]

class AttentionCreateSerializer(serializers.Serializer):
    pet_id = serializers.IntegerField()
    diagnosis = serializers.CharField()
    treatment = serializers.CharField()
    procedure = serializers.CharField()
    #imageUrl = serializers.URLField()
    
    
    def create(self, validated_data):
        record = AttentionModel(**validated_data)
        record.save()
        return record