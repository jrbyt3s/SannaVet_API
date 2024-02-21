from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, parsers, permissions
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import AttentionSerializer
from .models import AttentionModel


class AttetionView(generics.GenericAPIView):
    serializer_class = AttentionSerializer
    http_method_names = ['get', 'post']
    queryset = AttentionModel.objects
    #permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para listar las atenciones de la mascota',
        operation_description='ESte endpoint lista las atenciones de las mascotas'
    )
    def get(self, request):
        
        return Response({'status':'ok'}, status=status.HTTP_200_OK)