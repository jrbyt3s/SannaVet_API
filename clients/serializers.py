from rest_framework import serializers
from django.shortcuts import get_object_or_404
from users.models import UserModel
from pets.models import PetModel
from pets.serializers import PetSerializer

usuarios = UserModel.objects.all()
mascotas = PetModel.objects.all()

class ShoppingCartSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='product.id')
    name = serializers.CharField(source='product.name')
    price = serializers.DecimalField(
        max_digits=5, decimal_places=2, source='product.price'
    )
    image = serializers.URLField(source='product.image')
    quantity = serializers.IntegerField()

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source = 'user.username')
    email = serializers.CharField(source = 'user.email')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name =  serializers.CharField(source = 'user.last_name')
    role = serializers.CharField(source = 'user.role')
    mascotas = PetSerializer(many=True)




