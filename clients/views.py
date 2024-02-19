from django.http import JsonResponse
from django.views import View
from users.models import UserModel
from pets.models import PetModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        operation_summary='Endpoint para listar toda losusuarios relacionados con sus mascotas',
        operation_description='En este servicio retorna los usuarios y sus mascotas',
        
    )
class ClienteDataView(APIView):
    serializer_class = ClientSerializer
    http_method_names = ['get']

    def get(self, request):


        # Obteniendo datos de la base de datos
        usuarios = UserModel.objects.all()
        mascotas = PetModel.objects.all()

        # Formatea los datos según tu estructura JSON
        data = []
        for usuario in usuarios:
            usuario_data = {
                'id': usuario.id,
                'username': usuario.username,                
                'email': usuario.email,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'role':usuario.role,
                'mascotas': []
            }

            for mascota in mascotas.filter(user_id=usuario.id):
                mascota_data = {
                    'id': mascota.id,
                    'nombre': mascota.nombre,
                    'sexo': mascota.sexo,
                    'especie': mascota.especie,
                    'raza': mascota.raza,
                    'color': mascota.color,
                    'fotoUrl': mascota.fotoUrl,
                    'atenciones': [],
                    'citas': []
                }

               

                usuario_data['mascotas'].append(mascota_data)

            data.append({'usuario': usuario_data})

        # Devuelve la respuesta JSON
        if not data:
            return Response({'status':'nok'}, status=status.HTTP_404_NOT_FOUND)
    
        return Response(data, status=status.HTTP_200_OK)