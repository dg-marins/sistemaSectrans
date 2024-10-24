from django.contrib import admin
from .models import *

#Registra os modelos no admin
admin.site.register(Modelo_Equipamento)
admin.site.register(Empresa)
admin.site.register(Rede)


class CarrosAdmin(admin.ModelAdmin):
    # Para exibir campos no formulário de edição, mas não no cadastro
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # Se for um novo objeto (cadastro)
            fields.remove('ip')  # Remove o campo ip do cadastro
        return fields

    # Para garantir que o campo ip seja editável em edições
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None:  # Se for um objeto existente
            form.base_fields['ip'].required = False  # Permite edição do campo ip
        return form
    
admin.site.register(Carro, CarrosAdmin)

