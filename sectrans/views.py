# views.py
from django.shortcuts import render, get_object_or_404
from .models import Empresa, Carro
from django.http import JsonResponse

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
    
    # Se não for uma requisição AJAX, renderiza o template normalmente
    carros = Carro.objects.filter(empresa_id=empresa_id).order_by('nome')
    return render(request, 'listar_carros.html', {'empresa': empresa, 'carros': carros})

