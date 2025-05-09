from django.contrib import admin
from .models.modelo_equipamento import Modelo_Equipamento
from .models.empresa import Empresa
from .models.rede import Rede
from .models.carro import Carro
from .models.servidor import Servidor
from .models.video import Video

#Registra os modelos no admin
admin.site.register(Modelo_Equipamento)

class ListandoEmpresa(admin.ModelAdmin):
    list_display = ("id", "nome", "razao_social", "ativa",)
    list_display_links = ("nome", "razao_social",)
    list_editable = ("ativa",)

admin.site.register(Empresa, ListandoEmpresa)

class ListandoRedes(admin.ModelAdmin):
    list_display = ("id","nome", "chave", "empresa", "criptografia", "ip_servidor",)
    search_fields = ("nome",)

admin.site.register(Rede, ListandoRedes)

class CarrosAdmin(admin.ModelAdmin):

    list_display = ("id", "nome", "empresa", "rede", "modelo", "ip",)
    list_editable = ("ip",)
    list_filter = ("empresa", "rede", "modelo")
    search_fields = ['nome', 'ip']

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

class ServidoresAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "vpn", "ip_publico", "empresa",  "ativo")

admin.site.register(Servidor, ServidoresAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ("video_file", "carro", "channel","empresa", "data_video", "servidor", "tamanho", "duracao", "path_arquivo")

admin.site.register(Video, VideoAdmin)