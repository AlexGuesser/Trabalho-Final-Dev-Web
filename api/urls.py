from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('produtos', views.ProdutoList.as_view()),
    path('produtos/', views.ProdutoList.as_view()),
    path('promocoes', views.PromocaoList.as_view()),
    path('promocoes/', views.PromocaoList.as_view()),
    path('lojas', views.LojaList.as_view()),
    path('lojas/', views.LojaList.as_view()),
    path('produtos/<int:pk>', views.ProdutoDetail.as_view()),
    path('promocoes/<int:pk>', views.PromocaoDetail.as_view()),
    path('lojas/<int:pk>', views.LojaDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
