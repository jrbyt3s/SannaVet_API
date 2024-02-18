from django.urls import path
from .views import PetView

urlpatterns = [
    path('', PetView.as_view(), name='list_create')
]