from django.db import models

# Create your models here.

class PetModel(models.Model):
    nombre = models.CharField(max_length=50);
    sexo = models.CharField(max_length=1); #M / H
    especie = models.CharField(max_length=50);
    raza = models.CharField(default='mixta', max_length=50)
    color = models.CharField(max_length=50);
    fotoUrl = models.URLField(default='https://www.shutterstock.com/image-vector/animal-paw-print-vector-icon-260nw-1820447291.jpg')
    esterilizado = models.BooleanField(default=False)
    Peso = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    class Meta:
        db_table='pets'


