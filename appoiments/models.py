from django.db import models
from users.models import UserModel
from pets.models import PetModel
from datetime import datetime

class AppoimentModel(models.Model):
    pet = models.ForeignKey(PetModel, related_name='appoiments', on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(UserModel,on_delete = models.CASCADE, null=True)
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField()
    payed= models.BooleanField(default=False)
    state = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table='appoiments'
