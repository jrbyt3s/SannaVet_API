from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    # Agrega tus campos personalizados si los tienes

     # Sobreescribiendo atributos o columnas existentes
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [
        ('cliente', 'Cliente'),
        ('veterinario', 'Veterinario'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'