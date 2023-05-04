from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Boleia(models.Model):
    partida = models.CharField(max_length=255)
    chegada = models.CharField(max_length=255)
    horario = models.DateTimeField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    vagas = models.IntegerField()
    detalhes = models.TextField(blank=True)