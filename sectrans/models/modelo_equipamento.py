from django.db import models

class Modelo_Equipamento(models.Model):

    modelo = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Modelo Equipamento'
        verbose_name_plural = 'Modelos Equipamento'

    def __str__(self):
        return self.modelo