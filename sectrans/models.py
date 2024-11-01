from django.db import models
from django.core.exceptions import ValidationError
import re
from datetime import datetime

class Modelo_Equipamento(models.Model):

    modelo = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Modelo Equipamento'
        verbose_name_plural = 'Modelos Equipamento'

    def __str__(self):
        return self.modelo

class Empresa(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    razao_social = models.CharField(max_length=255, null=False, blank=False)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

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

class Carro(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=False)
    rede = models.ForeignKey(Rede, on_delete=models.SET_NULL, null=True, blank=False)
    modelo = models.ForeignKey(Modelo_Equipamento, on_delete=models.SET_NULL, null=True, blank=False)
    serial = models.CharField(max_length=30, blank=True)
    ip = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ip', 'rede'], name='unique_ip_per_rede'),
            models.UniqueConstraint(fields=['nome', 'empresa'], name='unique_carro_per_empresa')
        ]

    def clean(self):
        super().clean()  # Chama a limpeza do modelo pai

        # Validação do IP
        if not self.ip:
            if self.rede:
                self.ip = self.get_next_valid_ip()  # Preenche com o próximo IP válido
            else:
                raise ValidationError("A rede deve ser definida para atribuir um IP automaticamente.")
        else:
            self.validate_ip(self.ip)  # Valida o IP fornecido

    def validate_ip(self, value):
        # Padrão para qualquer IP válido
        pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})$'
        match = re.match(pattern, value)
        if not match:
            raise ValidationError('O IP deve estar no formato correto. xxx.xxx.xxx')

        if self.rede and value == self.rede.ip_servidor:
            raise ValidationError('O IP não pode ser o mesmo da rede.')
        
        last_octet = int(match.group(1))
        if last_octet > 254:
            raise ValidationError('O IP não pode ser maior que xxx.xxx.254')
        
    def get_next_valid_ip(self):
        """Retorna o próximo IP válido na rede associada."""
        utilizados = Carro.objects.filter(rede=self.rede).values_list('ip', flat=True)
        rede_ip_base = self.rede.ip_servidor.rsplit('.', 1)[0]  # Base do IP da rede
        ip_servidor = self.rede.ip_servidor

        for i in range(1, 255):
            next_ip = f"{rede_ip_base}.{i}"
            if next_ip not in utilizados and next_ip != ip_servidor:
                return next_ip
        raise ValidationError("Não há IPs disponíveis na rede.")
    
class Video(models.Model):
    video_file = models.CharField(max_length=100, null=True, blank=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=False, blank=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, blank=False)
    data_video = models.DateField(null=False, blank=False)
    hora_video = models.TimeField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    servidor = models.ForeignKey(Servidor, on_delete=models.SET_NULL, null=True, blank=True)
    erased = models.BooleanField(default=False)
    tamanho = models.IntegerField(null=True, blank=True, help_text="Tamanho do vídeo em MB")
    duracao = models.DurationField(null=True, blank=True)
    path_arquivo = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.carro.nome

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'
    