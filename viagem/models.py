from django.db import models

# Create your models here.

class Viagem(models.Model):
    nome_viagem = models.CharField(max_length=255)
    descricao = models.TextField()
    data_ida = models.DateField()
    data_retorno = models.DateField()

    def __str__(self):
        return self.nome_viagem

class Destino(models.Model):
    viagem = models.ForeignKey(Viagem, related_name='destinos', on_delete=models.CASCADE)
    nome_destino = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_destino
    