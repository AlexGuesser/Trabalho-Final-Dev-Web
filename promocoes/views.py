from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from .models import Promocao
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    lista_de_promocoes = Promocao.objects.order_by('id')[:30]
    context = { 'lista_de_promocoes': lista_de_promocoes }
    return render(request, 'promocoes/lista.html', context)

def detail(request, id):
    promocao_em_destaque = get_object_or_404(Promocao, pk=id)
    return render(request, 'promocoes/detail.html', { 'promocao_em_destaque': promocao_em_destaque })

def edit(request, id):
    promocao_em_destaque = get_object_or_404(Promocao, pk=id)
    return render(request, 'promocoes/edit.html', {'promocao_em_destaque': promocao_em_destaque })

def new(request):
    return render(request, 'promocoes/new.html', {})

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