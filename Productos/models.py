from os import set_inheritable
from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

class Productos(models.Model):
    
    
    marca = models.CharField(max_length= 100)
    serie = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    disponible = models.IntegerField()
    descripcion = models.TextField()
def __str__(self):
        return self.marca