from django.http import JsonResponse
from django.views import View
from users.models import UserModel
from pets.models import PetModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        print(records.query)
        serilizer = self.serializer_class(records, many=True)
               
        if not records:
            return Response({'status':'nok'}, status=status.HTTP_404_NOT_FOUND)
    
        return Response(serilizer.data, status=status.HTTP_200_OK)