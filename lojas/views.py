from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from .models import Loja
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    lista_de_lojas = Loja.objects.order_by('id')[:30]
    context = { 'lista_de_lojas': lista_de_lojas }
    return render(request, 'lojas/lista.html', context)

def detail(request, id):
    loja_em_destaque = get_object_or_404(Loja, pk=id)
    #user = authenticate(username='GerenteDeRede', password='senhateste')
    return render(request, 'lojas/detail.html', { 'loja_em_destaque': loja_em_destaque })

def edit(request, id):
    loja_em_destaque = get_object_or_404(Loja, pk=id)
    return render(request, 'lojas/edit.html', {'loja_em_destaque': loja_em_destaque })

def new(request):
    return render(request, 'lojas/new.html', {})

def do_login(request):
    proximapagina = request.POST['proximapagina']
    username = request.POST['usuario']
    password = request.POST['senha']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
    return HttpResponseRedirect(proximapagina)

def do_logout(request):
    logout(request)
    proximapagina = request.GET['proximapagina']
    return HttpResponseRedirect(proximapagina)