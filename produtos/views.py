from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    lista_de_produtos = Produto.objects.order_by('-id')
    context = { 'lista_de_produtos': lista_de_produtos }
    return render(request, 'produtos/lista.html', context)

def detail(request, id):
    produto_em_destaque = get_object_or_404(Produto, pk=id)
    return render(request, 'produtos/detail.html', { 'produto_em_destaque': produto_em_destaque })

def edit(request, id):
    if request.method == 'GET':
        produto_em_destaque = get_object_or_404(Produto, pk=id)
        formulario = ProdutoForm(instance=produto_em_destaque)
        return render(request, 'produtos/edit.html', {'produto_em_destaque': produto_em_destaque, 'formulario': formulario})
    if request.method == 'POST':
        produto_em_destaque = get_object_or_404(Produto, pk=id)
        formulario = ProdutoForm(request.POST, instance=produto_em_destaque)
        if formulario.is_valid():
            produto = formulario.save()
            return redirect('produtos:detail', id=produto.id)
        else:
            return render(request, 'produtos/edit.html', { 'formulario' : formulario })

def new(request):
    if request.method == 'GET':
        formulario = ProdutoForm()
        return render(request, 'produtos/new.html', { 'formulario': formulario })
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST)
        if formulario.is_valid():
            produto = formulario.save()
            return redirect('produtos:detail', id=produto.id)
        else:
            return render(request, 'produtos/new.html', { 'formulario' : formulario })