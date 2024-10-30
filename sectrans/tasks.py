from celery import shared_task
from .models import Empresa
from django.utils import timezone
import subprocess, os

@shared_task
def atualizar_status_vpn():
    empresas = Empresa.objects.all()  # Filtra apenas empresas ativas
    for empresa in empresas:
        vpn_ip = empresa.vpn
        vpn_ativa = is_ip_online(vpn_ip)

        empresa.vpn_status = vpn_ativa
        empresa.vpn_last_checked = timezone.now()
        empresa.save()

def is_ip_online(ip):
    try:
        # Executa o comando ping com 1 pacote (-c 1 para Unix, -n 1 para Windows)
        response = subprocess.run(
            ["ping", "-c", "1", ip] if os.name != 'nt' else ["ping", "-n", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Verifica o código de retorno. 0 significa que o IP está online
        return response.returncode == 0
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o IP {ip}: {e}")
        return False
    
@shared_task
def tarefa_teste():
    print("A tarefa foi executada!")
    return "A tarefa foi executada!"