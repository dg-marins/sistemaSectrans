from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='index'),
     path('selecionar-empresa/', views.selecionar_empresa, name='selecionar_empresa'),
     path('empresas/', views.listar_empresas, name='listar_empresas'),
     path('empresas/<int:empresa_id>/carros/', views.listar_carros, name='listar_carros'),
     path('login/', views.login_view, name='login'),
     path('logout/', views.listar_empresas, name='logout'),
]
