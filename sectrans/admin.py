from django.contrib import admin
from .models import *

#Registra os modelos no admin
admin.site.register(ModelosEquipamento)
admin.site.register(Empresas)
admin.site.register(Redes)

