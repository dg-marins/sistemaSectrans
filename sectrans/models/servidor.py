from .empresa import Empresa
from django.db import models

class Servidor(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    vpn = models.CharField(max_length=100, null=True, blank=True)
    ip_publico = models.CharField(max_length=100, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=False)
    vpn_status = models.BooleanField(default=False)
    vpn_last_checked = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.nome