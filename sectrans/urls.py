from django.urls import path
from .views import selecionar_empresa, listar_empresas

urlpatterns = [
     path('selecionar-empresa/', selecionar_empresa, name='selecionar_empresa'),
     path('empresas/', listar_empresas, name='listar_empresas'),
]