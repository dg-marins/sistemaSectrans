# views.py
from django.shortcuts import render
from .models import Empresa

def selecionar_empresa(request):
    return render(request, 'selecionar_empresa.html')

def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'selecionar_empresa.html', {'empresas': empresas})
