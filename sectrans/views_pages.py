# views.py
from django.shortcuts import render, redirect
from .models import Empresa, Carro, Modelo_Equipamento
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu')  # Redirecione para a página desejada após login bem-sucedido
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    
    return render(request, 'login.html')

def menu(request):
    return render(request, 'menu_principal.html')

def pedido_view(request):
    return render(request, 'pedido_midia.html')

def empresas_view(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'empresas.html', {'empresas': empresas})

def relatorio_cores_view(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'relatorio_cores.html', {'empresas': empresas})

def mapa_view(request):
    carros = Carro.objects.all()
    return render(request, 'mapa.html', {'carros': carros})