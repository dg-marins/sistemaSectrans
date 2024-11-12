from django.urls import path
from . import views_pages
from . import views_api

urlpatterns = [
    
    #Views
     path('', views_pages.login_view, name='index'),
     path('login/', views_pages.login_view, name='login'),
     path('menu/', views_pages.menu, name='menu'),
     path('pedido/', views_pages.pedido_view, name='pedido_view'),
     path('empresas_view/', views_pages.empresas_view, name='empresas_view'),
     path('relatorio_cores_view/', views_pages.relatorio_cores_view, name='relatorio_cores_view'),
     path('mapa/', views_pages.mapa_view, name='mapa_view'),
     path('logout/', views_pages.login_view, name='logout'),

     #Rest
     path('api/videos/register/', views_api.VideoRegister.as_view(), name='video_register'),
     path('api/empresas/', views_api.ListarEmpresas.as_view(), name='listar_empresas'),
     path('api/list_cars/<int:empresa_id>/', views_api.ListarCarrosByEmpresaId.as_view(), name='listar_carros'),
     path('api/list_equipament_models/', views_api.ListarModelosEquipamento.as_view(), name='listar_modelos'),
     path('api/list/channels/<int:empresa_id>', views_api.ListarCamsByEmpresaId.as_view(), name='listar_cameras'),
     path('api/list/relatorio_cores_info', views_api.ListarDadosRelatorioCores.as_view(), name="ListarDadosRelatorioCores")
     # path('videos/', views.VideoListView.as_view(), name='video_list'),

]
