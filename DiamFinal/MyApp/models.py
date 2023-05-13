from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
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