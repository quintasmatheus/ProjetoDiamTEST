from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser


# Create your models here.

# class CustomUser(AbstractUser):
#     MALE = 'M'
#     FEMALE = 'F'
#     GENDER_CHOICES = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#     ]
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     #password = models.CharField(max_length=128)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     phone_number = models.CharField(max_length=15)
#     car_brand = models.CharField(max_length=30)
#     car_model = models.CharField(max_length=30)

    # Adicione quaisquer outros campos ou métodos personalizados necessários

    #def __str__(self):
     #   return self.username




#def __str__(self):
  #  return f"{self.partida} - {self.chegada}"

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # MALE = 'M'
    # FEMALE = 'F'
    # GENDER_CHOICES = [
    #     (MALE, 'Male'),
    #     (FEMALE, 'Female'),
    # ]
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    # email = models.EmailField(unique=True)
    # #password = models.CharField(max_length=128)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #phone_number = models.CharField(max_length=15, null=True)
    car_brand = models.CharField(max_length=30, null=True)
    car_model = models.CharField(max_length=30, null=True)

class Boleia(models.Model):
    motorista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boleias_as_motorista')
    users = models.ManyToManyField(User, blank=True, related_name='boleias_as_passageiro')
    partida = models.CharField(max_length=255)
    chegada = models.CharField(max_length=255)
    horario = models.DateTimeField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    vagas = models.IntegerField()
    detalhes = models.TextField(blank=True)