from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from .models import Produto
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    lista_de_produtos = Produto.objects.order_by('id')[:30]
    context = { 'lista_de_produtos': lista_de_produtos }
    return render(request, 'produtos/lista.html', context)

def detail(request, id):
    produto_em_destaque = get_object_or_404(Produto, pk=id)
    #user = authenticate(username='GerenteDeRede', password='senhateste')
    return render(request, 'produtos/detail.html', { 'produto_em_destaque': produto_em_destaque })

def edit(request, id):
    produto_em_destaque = get_object_or_404(Produto, pk=id)
    return render(request, 'produtos/edit.html', {'produto_em_destaque': produto_em_destaque})

def new(request):
    return render(request, 'produtos/new.html', {})

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