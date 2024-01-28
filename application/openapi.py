from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


views = get_schema_view(
    openapi.Info(
        title='DRF Boilerplate',
        default_version='1.0',
        description='Endpoints del Boilerplate para Django Rest Framework'
    ),
    public=True
)


urlpatterns = [
    path('swagger-ui/', views.with_ui('swagger',
         cache_timeout=0), name='swagger-ui'),
    path('redoc/', views.with_ui('redoc',
         cache_timeout=0), name='redoc'),
]
