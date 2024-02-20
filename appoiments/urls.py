from django.urls import path
from .views import AppoimentView

urlpatterns = [
    path('', AppoimentView.as_view(), name='list_create'),
  #  path('<int:id>/',PetGetByIDView.as_view(), name='read_update_delete' )
]