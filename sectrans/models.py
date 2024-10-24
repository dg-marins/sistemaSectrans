from django.db import models
from datetime import datetime

class ModelosEquipamento(models.Model):

    modelo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.modelo
    
class Empresas(models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False)
    razao_social = models.CharField(max_length=255 , null=False, blank=False)
    vpn = models.CharField(max_length=100, default='')
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    ativa = models.BooleanField(default=True)

    # Relaciona o campo modelo com a tabela de modelo de equipamento
    modelo = models.ForeignKey(ModelosEquipamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Redes(models.Model):

    rede = models.CharField(max_length=20, null=False, unique=True, blank=False)
    chave = models.CharField(max_length=30, null=False, blank=False)
    ativa = models.BooleanField(default=True)
    empresa_id = models.IntegerField(null=False, blank=False)
    criptografia = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.rede