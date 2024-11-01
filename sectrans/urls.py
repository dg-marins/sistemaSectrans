from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='index'),
     path('login/', views.login_view, name='login'),
     path('menu/', views.menu, name='menu'),
     path('pedido/', views.pedido_view, name='pedido_view'),
     path('empresas_view/', views.empresas_view, name='empresas_view'),
     path('relatorio_cores_view/', views.relatorio_cores_view, name='relatorio_cores_view'),
     path('listar_empresas/', views.listar_empresas, name='listar_empresas'),
     path('listar_carros/<int:empresa_id>/', views.listar_carros, name='listar_carros'),
     path('listar_modelos/', views.listar_modelos, name='listar_modelos'),
     path('logout/', views.login_view, name='logout'),
]
