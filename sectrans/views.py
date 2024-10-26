# views.py
from django.shortcuts import render, get_object_or_404, redirect
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
            return redirect('pedido_midia')  # Redirecione para a página desejada após login bem-sucedido
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    
    return render(request, 'login.html')

def pedido_midia(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'pedido_midia.html', {'empresas': empresas})

def listar_modelos(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    
    # Verificando se a requisição é AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        modelos = Modelo_Equipamento.objects.filter(veiculo=carro).order_by('modelo').values('id', 'modelo')
        return JsonResponse({'modelos': list(modelos)})