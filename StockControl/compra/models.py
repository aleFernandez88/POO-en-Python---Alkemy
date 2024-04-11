from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=10)
    stock_actual = models.IntegerField(max_length=50)
    
    
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=8)