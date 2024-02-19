from django.urls import path
from .views import PetView, PetGetByIDView

urlpatterns = [
    path('', PetView.as_view(), name='list_create'),
    path('<int:id>/',PetGetByIDView.as_view(), name='read_update_delete' )
]