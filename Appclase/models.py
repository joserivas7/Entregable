from django.db import models
from datetime import datetime, date


# Create your models here.


class familia (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    parentesco= models.CharField(max_length=20)
    edad= models.IntegerField()
    fecha_nacimineto= models.DateField(auto_created=False, auto_now=False, blank=True)