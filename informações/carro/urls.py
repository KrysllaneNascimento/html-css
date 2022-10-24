from django.urls import path
from . import views 
from .views import *


app_name = 'carro'

urlpatterns = [
    path('inicial/', views.principal, name='inicial'),
    path('cadastro_veiculo/', Cadastrar_veiculo.as_view(), name='cadastro_veiculo'),
    path('abastecer/', Abastecer_veiculo.as_view(), name='abastecer_veiculo'),
    path('despesas/', Despesas.as_view(), name='despesas_veiculo'),
    path('troca_oleo/', Troca_Oleo.as_view(), name='troca_oleo'),
    path('usuario/', views.usuario, name='usuario'),
    path('logout',views.logout_view,name='logout'),
]


