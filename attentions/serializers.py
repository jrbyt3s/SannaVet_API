from rest_framework import serializers
from django.shortcuts import get_list_or_404
from .models import AttentionModel
from datetime import datetime
from django.shortcuts import get_object_or_404
from application.utils.bucket import Bucket
from django.utils.text import slugify

IMAGE_EXTENSION = '.png'

class AttentionSerializer(serializers.ModelSerializer):
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
    
class AttentionUpdateSerializer(serializers.Serializer):
    #pet_id = serializers.IntegerField()
    diagnosis = serializers.CharField()
    treatment = serializers.CharField()
    procedure = serializers.CharField()
    imageUrl = serializers.ImageField()

    def update(self, instance, validated_data):
        image = validated_data.get('imageUrl')
       
        
        #name = validated_data.get('nombre') or instance.name
        name = f'atencionID-{instance.id}-'

        if image:
            bucket = Bucket('drfecommercee', 'atenciones')
            name = name+image._name.split('.')[0]
            print(name)
            url = bucket.upload_object(
                f'{slugify(name)}{IMAGE_EXTENSION}', image.file
            )
            validated_data['imageUrl'] = url

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class AttencionDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def deactivate(self):
        pet_id = self.validated_data['id']
        record = get_object_or_404(AttentionModel, pk=pet_id, is_delete=False)
        record.is_delete=True
        record.save()