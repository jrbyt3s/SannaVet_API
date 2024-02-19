from rest_framework import serializers
from .models import PetModel
from application.utils.bucket import Bucket
from django.utils.text import slugify
from django.shortcuts import get_object_or_404


IMAGE_EXTENSION = '.png'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = '__all__'

class PetCreateSerializer(serializers.Serializer):
    nombre =serializers.CharField(max_length=50);
    sexo = serializers.CharField(default='m', max_length=1); #M / H
    especie = serializers.CharField(max_length=50);
    raza = serializers.CharField(default='mixta')
    color = serializers.CharField(max_length=50);
    fotoUrl = serializers.ImageField(write_only=True)
    esterilizado = serializers.BooleanField(default=False)
    peso = serializers.DecimalField(default=0.0, max_digits=3, decimal_places=1)

    def create(self, validated_data):
        bucket = Bucket('drfecommercee', 'pets')

        image = validated_data['fotoUrl']
        name = validated_data['nombre']
        url = bucket.upload_object(
            f'{slugify(name)}{IMAGE_EXTENSION}', image.file
        )
        validated_data['fotoUrl'] = url
        record = PetModel(**validated_data)
        record.save()
        return record

class PetUpdateSerializer(serializers.Serializer):
    nombre =serializers.CharField(max_length=50, required=False);
    sexo = serializers.CharField(default='m', max_length=1, required=False); #M / H
    especie = serializers.CharField(max_length=50, required=False);
    raza = serializers.CharField(default='mixta', required=False)
    color = serializers.CharField(max_length=50, required=False);
    fotoUrl = serializers.ImageField(write_only=True, required=False)
    esterilizado = serializers.BooleanField(default=False, required=False)
    peso = serializers.DecimalField(default=0.0, max_digits=3, decimal_places=1, required=False)

    def update(self, instance, validated_data):
        image = validated_data.get('fotoUrl')
        petid = instance.id
        name = validated_data.get('nombre') or instance.name
        name = f'{name}-petid-{petid}'

        if image:
            bucket = Bucket('drfecommercee', 'pets')
            url = bucket.upload_object(
                f'{slugify(name)}{IMAGE_EXTENSION}', image.file
            )
            validated_data['fotoUrl'] = url

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
class PetDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def deactivate(self):
        pet_id = self.validated_data['id']
        record = get_object_or_404(PetModel, pk=pet_id, is_delete=False)
        record.is_delete=True
        record.save()