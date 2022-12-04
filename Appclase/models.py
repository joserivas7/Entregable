from django.db import models



# Create your models here.


class familia (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    parentesco= models.CharField(max_length=20)
    edad= models.IntegerField()