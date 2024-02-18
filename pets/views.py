from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import PetSerializer
from .models import PetModel
from .schemas import PetSchema

class PetView(generics.GenericAPIView):
    serializer_class = PetSerializer
    http_method_names = ['get', 'post']
    queryset = PetModel.objects

    @swagger_auto_schema(
        operation_summary='Endpoint para listar las mascotas',
        operation_description='En este servicio retorna todas las Mascotas en el sistema',
        #manual_parameters=schema_request.all()
    )
    def get(self, request):
        pass
    
    @swagger_auto_schema(
        operation_summary='Endpoint para crear una mascota en el sistema',
        operation_description='En este servicio crea una mascota',
        #manual_parameters=schema_request.all()
    )
    def post(selft, request):
        pass
