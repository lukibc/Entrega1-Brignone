from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField(max_length=50)

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField(max_length=50)
    profesion=models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()