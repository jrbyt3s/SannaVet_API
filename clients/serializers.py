from rest_framework import serializers
from django.shortcuts import get_object_or_404
from users.models import UserModel
from pets.models import PetModel
from pets.serializers import PetSerializer
from users.serializers import UserSerializer
from appoiments.serializers import AppoimentSerializer

usuarios = UserModel.objects.all()
mascotas = PetModel.objects.all()



class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    role = serializers.CharField(max_length=20)
    pets = PetSerializer(many=True)
    

    
    





