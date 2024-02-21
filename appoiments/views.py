from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, parsers, permissions
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import AppoimentSerializer, AppoimentCreateSerializer, AppoimentUpdateSerializer, AppoimentDeleteSerializer
from .models import AppoimentModel
from .schemas import Appoimentchema

schema_request = Appoimentchema()

class AppoimentView(generics.GenericAPIView):
    serializer_class = AppoimentSerializer
    http_method_names = ['get', 'post']
    queryset = AppoimentModel.objects
    #permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para listar las citas',
        operation_description='En este servicio retorna todas las citas',
        manual_parameters=schema_request.all()
    )
    def get(self, request):
        # Query params
        query_params = request.query_params
        nro_page = query_params.get('page')
        if nro_page is None: nro_page = 1
        per_page = query_params.get('per_page')
        if per_page is None: per_page = 20
        query = query_params.get('q', '')


        # Filtros por defecto
        filters = {'is_delete': False}
            
        records = self.queryset.filter(**filters).filter(
            Q(id__icontains=query) 
        ).order_by('-id')
        print(records.query)
        serilizer = self.serializer_class(records, many=True)

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
        operation_summary='Endpoint para Crear las citas',
        operation_description='En este servicio permite crear una cita, pero necesita el id de mascota, y el id del veterinario ',
        request_body=AppoimentCreateSerializer
    )
    def post(self, request):
        serializer = AppoimentCreateSerializer(data= request.data) 
        # print(serializer.__dict__)
   
        #print(request.data)       
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class AppoimentGetByIdView(generics.GenericAPIView):
    serializer_class = AppoimentSerializer
    http_method_names = ['get', 'patch', 'delete']
    queryset = AppoimentModel.objects
    #permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para obtener una cita por el ID',
        operation_description='En este servicio se obtendra una cita, pero necesitas el id de la cita'
    )
    def get(self, _, id):
        record = get_object_or_404(self.queryset, pk=id, is_delete=False)
        serializer = self.serializer_class(record, many=False)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        record = get_object_or_404(self.queryset, pk=id, is_delete=False)
        serializer = AppoimentUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_summary='Endpoint para inactivar una cita por el ID',
        operation_description='En este servicio se inactiva una cita por el id'
    )
    def delete(self, _, id):
        serializer = AppoimentDeleteSerializer(data={'id':id})
        serializer.is_valid(raise_exception=True)
        serializer.deactivate()
        return Response(status=status.HTTP_204_NO_CONTENT)
    