from django.urls import path
from .views import AliveView


urlpatterns = [
    path('', AliveView.as_view(), name='get_alive'),
    
]