from django.db import models
from users.models import UserModel

# Create your models here.

class PetModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE )
    nombre = models.CharField(max_length=50);
    sexo = models.CharField(max_length=1); #M / H
    especie = models.CharField(max_length=50);
    raza = models.CharField(default='mixta', max_length=50)
    color = models.CharField(max_length=100);
    fotoUrl = models.URLField(default='https://www.shutterstock.com/image-vector/animal-paw-print-vector-icon-260nw-1820447291.jpg')
    esterilizado = models.BooleanField(default=False)
    peso = models.DecimalField( default=0.0, max_digits=3, decimal_places=1)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table='pets'


