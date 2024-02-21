from django.urls import path
from .views import AttetionView

urlpatterns = [
    path('', AttetionView.as_view(), name='list_create'),
]