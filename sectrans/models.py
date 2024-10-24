from django.db import models
from datetime import datetime

class ModeloEquipamentos(models.Model):

    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.modelo
    
class Empresa(models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False)
    razao_social = models.CharField(max_length=255 , null=False, blank=False)
    vpn = models.CharField(max_length=100, default='')
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    ativa = models.BooleanField(default=True)
    
    # Relaciona o campo modelo com a tabela de modelo de equipamento
    modelo = models.ForeignKey(ModeloEquipamentos, on_delete=models.SET_NULL, null=True, blank=True)

