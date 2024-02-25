from rest_framework import serializers
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import UserModel
from secrets import token_hex
from application.utils.mailing import Mailing
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    tokens = serializers.SerializerMethodField()

    def action(self):
        username = self.validated_data['username']
        password = self.validated_data['password']

        user = authenticate(username=username, password=password)
        jwt = RefreshToken.for_user(user)
        
        token_data = {
            'username': user.username,
            'email': user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role
        }
        jwt.payload.update(token_data)
    
        return {            
            'access_token': str(jwt.access_token),
            'refresh_token': str(jwt)
        }

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not authenticate(username=username, password=password):
            raise AuthenticationFailed()

        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def action(self):
        mailing = Mailing()

        email = self.validated_data['email']
        new_password = token_hex(5)

        record = get_object_or_404(
            UserModel, email=email, is_active=True, is_staff=False
        )
        record.set_password(new_password)
        record.save()

        mailing.mail_reset_password(
            record.email, record.first_name, new_password
        )

        return {
            'message': 'Password Reset Succesfull'
        }


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128)

    def update(self, instance, validated_data):
        new_password = validated_data['new_password']
        instance.set_password(new_password)
        instance.save()
        return instance
