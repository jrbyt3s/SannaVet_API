from rest_framework.viewsets import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, ResetPasswordSerializer, ChangePasswordSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary='Endpoint para autenticarse',
        operation_description='En este endpoint podras generar los token de acceso',
        security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.action()
        return Response(response, status=status.HTTP_200_OK)


class RefreshTokenView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_summary='Endpoint para crear un nuevo access_token',
        operation_description='En este servicio podemos generar un nuevo token desde el refresh_token',
        security=[]
    )
    def post(self, request):
        return super().post(request)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(
        operation_summary='Endpoint para resetear la contraseña',
        operation_description='En este servicio se enviara un correo con la nueva contraseña',
        security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.action()
        return Response(response, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para cambiar la contraseña',
        operation_description='En este servicio se podra actualizar la contraseña del usuario conectado'
    )
    def put(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
