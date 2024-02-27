from django.http import JsonResponse
from django.views import View
from users.models import UserModel
from pets.models import PetModel
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, parsers, permissions
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema


class ClienteDataView(APIView):
    serializer_class = ClientSerializer
    queryset = UserModel.objects
    
    http_method_names = ['get']


    @swagger_auto_schema(
        operation_summary='Endpoint para listar toda losusuarios relacionados con sus mascotas',
        operation_description='En este servicio retorna los usuarios y sus mascotas',
        
    )
    def get(self, request):
        records = self.queryset.all().prefetch_related('pets')
        serilizer = self.serializer_class(records, many=True)
               
        if not records:
            return Response({'status':'nok'}, status=status.HTTP_404_NOT_FOUND)
    
        return Response(serilizer.data, status=status.HTTP_200_OK)
    

class ClienteDataByIDView(generics.GenericAPIView):
    serializer_class = ClientSerializer
    http_method_names = ['get']
    queryset = UserModel.objects
    #parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para lista la data por id',
        operation_description='Este servicio retorna toda la dat relacionada a un usuario',
        
    )
    def get(self, _, id):
        record = get_object_or_404(self.queryset, pk=id, is_active=True)
        serializer = self.serializer_class(record, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)