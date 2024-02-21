from django.urls import path
from .views import AppoimentView, AppoimentGetByIdView

urlpatterns = [
    path('', AppoimentView.as_view(), name='list_create'),
    path('<int:id>/',AppoimentGetByIdView.as_view(), name='read_update_delete' )
]