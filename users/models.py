from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    # Sobreescribiendo atributos o columnas existentes
    email = models.EmailField(unique=True)

    # Crear nuevos atributos o columnas
    # auto_now_add -> inserta la fecha y la hora actual, solo en la creación
    # auto_now -> insertar la fecha y la hora actual, por cada cambio realizado
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        # ordering = ['-id']
