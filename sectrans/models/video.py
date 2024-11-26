from django.db import models
from django.utils import timezone
from carro import Carro
from empresa import Empresa
from servidor import Servidor


class Video(models.Model):
    video_file = models.CharField(max_length=100, null=True, blank=False)
    channel = models.IntegerField(null=True, blank=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=False, blank=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, blank=False)
    data_video = models.DateField(null=False, blank=False)
    hora_video = models.TimeField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    servidor = models.ForeignKey(Servidor, on_delete=models.SET_NULL, null=True, blank=True)
    erased = models.BooleanField(default=False)
    tamanho = models.FloatField(null=True, blank=True, help_text="Tamanho do vídeo em KB")
    duracao = models.DurationField(null=True, blank=True, help_text="Duração do vídeo em segundos")
    path_arquivo = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.carro.nome

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

        constraints = [
            models.UniqueConstraint(fields=['video_file', 'channel', 'carro', 'data_video'], name='unique_file_per_channel_in_car_at_date'),
        ]
    