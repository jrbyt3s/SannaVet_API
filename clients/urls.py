from django.urls import path
from .views import ClienteDataView

urlpatterns = [
    path('', ClienteDataView.as_view(), name='list_create'),
    
]