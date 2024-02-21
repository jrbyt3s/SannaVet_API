from rest_framework import serializers
from django.shortcuts import get_list_or_404
from .models import AttentionModel


class AttentionSerializer(serializers.Serializer):
    class Meta:
        model =AttentionModel
        fields = [
            "id","pet", "diagnosis", "treatment",
            "procedure", "imageUrl","dateOfAttention",
        ]