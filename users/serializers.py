from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name', 'role',
        ]


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    role = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data): #existe en la clase padre, aqui lo reescribimos
        password = validated_data['password'] # extraemos es password
        record = UserModel(**validated_data) #Qwars con diccionario validate_data
        record.set_password(password) # encriptamos la contraseña con un metodo interno
        record.save()
        return record


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    role = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def deactivate(self):
        user_id = self.validated_data['id']
        record = get_object_or_404(
            UserModel, pk=user_id, is_active=True, is_staff=False
        )
        record.is_active = False
        record.save()
