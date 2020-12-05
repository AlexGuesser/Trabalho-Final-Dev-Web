from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [
    path('', views.index, name='index'), #Lista de produtos
    path('<int:id>/', views.detail, name='detail'), #Detalhes do produto
    path('<int:id>/edit/', views.edit, name='edit'), #Editar produto
    path('new/', views.new, name='new'), #Criar produto
]