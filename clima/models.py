from django.db import models
from viagem.models import Viagem

# Create your models here.

class Clima(models.Model):
    viagem = models.OneToOneField(Viagem, on_delete=models.CASCADE)
    temperatura = models.FloatField()
    condicoes_climaticas = models.CharField(max_length=255)

    def __str__(self):
        return f"O clima para {self.viagem.nome_viagem}"