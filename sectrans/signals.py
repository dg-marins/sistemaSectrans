from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import re
from .models import Carros


# Função de validação personalizada para o último octeto do IP
def validate_ip(value):
    # Padrão para qualquer IP válido
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})$'
    match = re.match(pattern, value)
    
    # Verifica se o IP corresponde ao padrão
    if not match:
        raise ValidationError('O IP deve estar no formato correto.')

    last_octet = int(match.group(1))
    
    # Verifica se o último octeto é maior que 254
    if last_octet > 254:
        raise ValidationError('O último octeto do IP não pode ser maior que 254.')

@receiver(pre_save, sender=Carros)
def validate_carros_ip(sender, instance, **kwargs):
    validate_ip(instance.ip)