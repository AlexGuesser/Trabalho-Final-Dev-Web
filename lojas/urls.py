from django.urls import path
from . import views

app_name = 'lojas'
urlpatterns = [
    path('', views.index, name='index'), #Lista
    path('<int:id>/', views.detail, name='detail'), #Detalhes
    path('<int:id>/edit/', views.edit, name='edit'), #Editar
    path('new/', views.new, name='new'), #Criar
]