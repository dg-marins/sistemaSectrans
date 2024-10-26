from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='index'),
     path('login/', views.login_view, name='login'),
     path('pedido_midia/', views.pedido_midia, name='pedido_midia'),
     path('listar_carros/<int:empresa_id>/', views.listar_carros, name='listar_carros'),
     path('logout/', views.login_view, name='logout'),
]
