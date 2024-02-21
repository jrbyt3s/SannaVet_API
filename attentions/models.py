from django.db import models
from pets.models import PetModel
from datetime import datetime

class AttentionModel(models.Model):
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    procedure = models.TextField()
    imageUrl = models.URLField()
    dateOfAttention = models.DateTimeField(default=datetime.now)
    is_delete = models.BooleanField(default=False)
