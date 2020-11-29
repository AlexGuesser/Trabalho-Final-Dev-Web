from django.urls import path
from . import views

app_name = 'promocoes'
urlpatterns = [
    path('', views.index, name='index'), #Lista de promocoes
    path('<int:id>/', views.detail, name='detail'), #Detalhes da promoção
    path('<int:id>/edit/', views.edit, name='edit'), #Editar promoção
    path('new/', views.new, name='new'), #Criar promoção-
    path('do_login/', views.do_login, name='do_login'), #Login
    path('do_logout/', views.do_logout, name='do_logout'), #Logout

]