from rest_framework import serializers
from .models import PetModel
from application.utils.bucket import Bucket
from django.utils.text import slugify


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
