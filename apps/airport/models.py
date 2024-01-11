from django.db import models

# Create your models here.
from apps.common.models import BaseModel


class Airport(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
