# views.py
from django.shortcuts import render

def selecionar_empresa(request):
    return render(request, 'selecionar_empresa.html')