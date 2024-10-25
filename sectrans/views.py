# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, Carro, Modelo_Equipamento
from django.http import JsonResponse

from django.contrib.auth import authenticate, login
from django.contrib import messages

def selecionar_empresa(request):
    return render(request, 'selecionar_empresa.html')

def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'selecionar_empresa.html', {'empresas': empresas})

def listar_carros(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    # Verificando se a requisição é AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        carros = Carro.objects.filter(empresa_id=empresa_id).order_by('nome').values('id', 'nome')
        return JsonResponse({'carros': list(carros)})
    
    carros = Carro.objects.filter(empresa_id=empresa_id).order_by('nome')
    return render(request, 'listar_carros.html', {'empresa': empresa, 'carros': carros})

def listar_modelos(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    
    # Verificando se a requisição é AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        modelos = Modelo_Equipamento.objects.filter(veiculo=carro).order_by('modelo').values('id', 'modelo')
        return JsonResponse({'modelos': list(modelos)})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('listar_empresas')  # Redirecione para a página desejada após login bem-sucedido
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'login.html')