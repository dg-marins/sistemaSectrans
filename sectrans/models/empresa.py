from django.db import models
from django.utils import timezone

class Empresa(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    razao_social = models.CharField(max_length=255, null=False, blank=False)
    data_cadastro = models.DateTimeField(default=timezone.now, blank=False)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome