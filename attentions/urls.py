# urls.py
from django.urls import path
from .views import AttentionView

urlpatterns = [
    path('', AttentionView.as_view(), name='list_create'),
    
]