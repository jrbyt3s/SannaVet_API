# urls.py
from django.urls import path
from .views import AttentionView, AttentionByIDView

urlpatterns = [
    path('', AttentionView.as_view(), name='list_create'),
    path('<int:id>/',AttentionByIDView.as_view(), name='read_update_delete' )
]