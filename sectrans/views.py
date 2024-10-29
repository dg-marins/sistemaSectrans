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
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('menu')  # Redirecione para a página desejada após login bem-sucedido
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    
    return render(request, 'login.html')

def menu(request):
    return render(request, 'menu_principal.html')

def pedido_view(request):
    return render(request, 'pedido_midia.html')

def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'empresas.html', {empresas: empresas})

def listar_modelos(request):
    modelos = Modelo_Equipamento.objects.all().order_by('modelo').values('id', 'modelo')
    return JsonResponse(list(modelos), safe=False)
    
def listar_carros(request, empresa_id):
    carros = Carro.objects.filter(empresa_id=empresa_id).values('id', 'nome')
    return JsonResponse(list(carros), safe=False)