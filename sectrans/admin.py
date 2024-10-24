from django.contrib import admin
from .models import *

#Registra os modelos no admin
admin.site.register(Modelo_Equipamento)
admin.site.register(Empresa)
admin.site.register(Rede)
admin.site.register(Carro)

