from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDeleteSerializer
from .models import UserModel
from .schemas import UserSchema


schema_request = UserSchema()


class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']
    queryset = UserModel.objects
    # permission_classes = [permissions.IsAuthenticated]

    # TODO: Definición de permisos por verbo HTTP
    # def get_permissions(self):
    #    if self.request.method == 'POST':
    #        return [permissions.IsAuthenticated()]
    #    return [permissions.AllowAny()]

    @swagger_auto_schema(
        operation_summary='Endpoint para listar los usuarios',
        operation_description='En este servicio retorna todos los usuarios',
        manual_parameters=schema_request.all()
    )
    def get(self, request):
        # Query params
        query_params = request.query_params
        nro_page = query_params.get('page')
        per_page = query_params.get('per_page')
        query = query_params.get('q', '')

        # Filtros por defecto
        filters = {'is_staff': False, 'is_active': True}

        records = self.queryset.filter(**filters).filter(
            Q(first_name__icontains=query) |
            Q(username__icontains=query) |
            Q(last_name__icontains=query)
        ).order_by('-id')

        # Inicializar la class Paginator
        paginator = Paginator(records, per_page=per_page)
        page = paginator.get_page(nro_page)

        # Atributos de la paginación
        serializer = self.serializer_class(page.object_list, many=True)

        return Response({
            'results': serializer.data,
            'pagination': {
                'totalRecords': paginator.count,
                'totalPages': paginator.num_pages,
                'perPage': paginator.per_page,
                'currentPage': page.number
            }
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Endpoint para crear un usuario',
        operation_description='En este servicio se creara un usuario',
        request_body=UserCreateSerializer
    )
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# /users/:id
class UserGetByIdView(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']
    queryset = UserModel.objects
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para obtener un usuario por el ID',
        operation_description='En este servicio se obtendra un usuario'
    )
    def get(self, _, id):
        record = get_object_or_404(
            self.queryset, pk=id, is_active=True, is_staff=False
        )
        serializer = self.serializer_class(record, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Endpoint para actualizar un usuario por el ID',
        operation_description='En este servicio se actualizara el usuario',
        request_body=UserUpdateSerializer
    )
    def patch(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id, is_active=True, is_staff=False
        )
        serializer = UserUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Endpoint para inactivar un usuario por el ID',
        operation_description='En este servicio se inactivara el usuario'
    )
    def delete(self, _, id):
        serializer = UserDeleteSerializer(data={'id': id})
        serializer.is_valid(raise_exception=True)
        serializer.deactivate()
        return Response(status=status.HTTP_204_NO_CONTENT)
