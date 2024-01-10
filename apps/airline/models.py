from django.db import models

from apps.common.models import BaseModel


class Airline(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5, unique=True)
    logo = models.PositiveIntegerField
