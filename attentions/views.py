from rest_framework.viewsets import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, parsers, permissions
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import AttentionSerializer, AttentionCreateSerializer
from .models import AttentionModel
from .schemas import AttentionSchema


schema_request = AttentionSchema()

class AttentionView(generics.GenericAPIView):
    serializer_class = AttentionSerializer
    http_method_names = ['get', 'post']
    queryset = AttentionModel.objects
    #permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para listar las atenciones de la mascota',
        operation_description='ESte endpoint lista las atenciones de las mascotas',
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
            Q(id__icontains=query,
              diagnosis__icontains=query,
              treatment__icontains=query,
              procedure__icontains=query,
              dateOfAttention__icontains=query,
              ) 
        ).order_by('-id')
        
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
            operation_summary='Endpoint para crear Atenciones clinicas',
            operation_description='en este enpoint se registran las atenciones clínicas de las mascotas, se necesita el Pet_id',
            request_body=AttentionCreateSerializer
    )
    def post(self, request):
        serializer = AttentionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data= serializer.data, status=status.HTTP_201_CREATED)