from django.db import models
from .empresa import Empresa

class Rede(models.Model):
    CRIPTOGRAFIA = {"WPA": "WPA", "WEP": "WEP"}

    nome = models.CharField(max_length=20, null=False, unique=True, blank=False)
    chave = models.CharField(max_length=30, null=False, blank=False)
    ativa = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    criptografia = models.CharField(choices=CRIPTOGRAFIA, null=False, blank=False)
    ip_servidor = models.CharField(max_length=11, null=False, blank=False, default='192.168.0.1')

    def __str__(self):
        return self.nome