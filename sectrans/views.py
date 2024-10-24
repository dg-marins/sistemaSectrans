# views.py
from django.shortcuts import render, get_object_or_404
from .models import Empresa, Rede, Carro

def selecionar_empresa(request):
    empresas = Empresa.objects.all()  # Buscando todas as empresas
    redes = None
    carros = None

    if request.method == 'POST':
        empresa_id = request.POST.get('empresa_id')
        empresa = get_object_or_404(Empresa, id=empresa_id)
        redes = Rede.objects.filter(empresa=empresa)  # Buscando redes da empresa selecionada

        if 'rede_id' in request.POST:
            rede_id = request.POST.get('rede_id')
            rede = get_object_or_404(Rede, id=rede_id)
            carros = Carro.objects.filter(rede=rede)  # Buscando carros da rede selecionada

    return render(request, 'selecionar_empresa.html', {
        'empresas': empresas,
        'redes': redes,
        'carros': carros,
    })
