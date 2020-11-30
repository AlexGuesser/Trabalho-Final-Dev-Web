from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Loja
from .forms import LojaForm

# Create your views here.

def index(request):
    lista_de_lojas = Loja.objects.order_by('id')[:30]
    context = { 'lista_de_lojas': lista_de_lojas }
    return render(request, 'lojas/lista.html', context)

def detail(request, id):
    loja_em_destaque = get_object_or_404(Loja, pk=id)
    return render(request, 'lojas/detail.html', { 'loja_em_destaque': loja_em_destaque })

def edit(request, id):
    if request.method == 'GET':
        loja_em_destaque = get_object_or_404(Loja, pk=id)
        formulario = LojaForm(instance=loja_em_destaque)
        return render(request, 'lojas/edit.html', {'loja_em_destaque': loja_em_destaque, 'formulario': formulario})
    if request.method == 'POST':
        loja_em_destaque = get_object_or_404(Loja, pk=id)
        formulario = LojaForm(request.POST, instance=loja_em_destaque)
        if formulario.is_valid():
            loja = formulario.save()
            return redirect('lojas:detail', id=loja.id)
        else:
            return render(request, 'lojas/edit.html', { 'formulario' : formulario })

def new(request):
    if request.method == 'GET':
        formulario = LojaForm()
        return render(request, 'lojas/new.html', { 'formulario': formulario })
    if request.method == 'POST':
        formulario = LojaForm(request.POST)
        if formulario.is_valid():
            loja = formulario.save()
            return redirect('lojas:detail', id=loja.id)
        else:
            return render(request, 'lojas/new.html', { 'formulario' : formulario })


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