from django.db import models
from django.db import models
from django.contrib.auth.models import User

from django import forms
# Create your models here.

class Peaple(models.Model):  
    id = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    

    def __str__(self) -> str:
        return self.nome
    


class Devices(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    
    
    

    def __str__(self) -> str:
        return self.nome


class DevicesControl(models.Model):
    id = models.AutoField(primary_key=True)  
    peaple = models.ForeignKey(Peaple, on_delete=models.CASCADE)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    
    

    def __str__(self) -> str:
        return self.nome

