from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Promocao
from .forms import PromocaoForm, PromocaoEditForm

# Create your views here.

def index(request):
    lista_de_promocoes = Promocao.objects.order_by('id')[:30]
    context = { 'lista_de_promocoes': lista_de_promocoes }
    return render(request, 'promocoes/lista.html', context)

def detail(request, id):
    promocao_em_destaque = get_object_or_404(Promocao, pk=id)
    return render(request, 'promocoes/detail.html', { 'promocao_em_destaque': promocao_em_destaque })

def edit(request, id):
    if request.method == 'GET':
        promocao_em_destaque = get_object_or_404(Promocao, pk=id)
        formulario = PromocaoEditForm(instance=promocao_em_destaque)
        return render(request, 'promocoes/edit.html', {'promocao_em_destaque': promocao_em_destaque, 'formulario' : formulario })
    if request.method == 'POST':
        promocao_em_destaque = get_object_or_404(Promocao, pk=id)
        formulario = PromocaoEditForm(request.POST, instance=promocao_em_destaque)
        if formulario.is_valid():
            promocao = formulario.save()
            return redirect('promocoes:detail', id=promocao.id)
        else:
            return render(request, 'promocoes/edit.html', { 'promocao_em_destaque' : promocao_em_destaque })

def new(request):
    if request.method == 'GET':
        formulario = PromocaoForm()
        return render(request, 'promocoes/new.html', { 'formulario': formulario })
    if request.method == 'POST':
        formulario = PromocaoForm(request.POST)
        if formulario.is_valid():
            promocao = formulario.save()
            return redirect('promocoes:detail', id=promocao.id)
        else:
            return render(request, 'promocoes/new.html', { 'formulario' : formulario })

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