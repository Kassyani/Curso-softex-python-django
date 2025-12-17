
from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media'
    )

    prazo = models.DateField(null=True, blank=True)

    concluida = models.BooleanField(default=False)

    deletada = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
