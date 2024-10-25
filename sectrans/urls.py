from django.urls import path
from . import views

urlpatterns = [
     path('selecionar-empresa/', views.selecionar_empresa, name='selecionar_empresa'),
     path('empresas/', views.listar_empresas, name='listar_empresas'),
     path('empresas/<int:empresa_id>/carros/', views.listar_carros, name='listar_carros'),
]