from django.urls import path
from .views import UserView, UserGetByIdView


urlpatterns = [
    path('', UserView.as_view(), name='list_create'),
    path('<int:id>/', UserGetByIdView.as_view(), name='read_update_delete')
]
