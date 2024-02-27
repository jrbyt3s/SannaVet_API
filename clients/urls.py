from django.urls import path
from .views import ClienteDataView, ClienteDataByIDView

urlpatterns = [
    path('', ClienteDataView.as_view(), name='list_create'),
    path('<int:id>/',ClienteDataByIDView.as_view(), name ='read' )
]