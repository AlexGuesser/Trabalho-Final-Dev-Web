from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect #HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Promocao
from lojas.models import Loja
from produtos.models import Produto
from .forms import PromocaoForm, PromocaoEditForm

# Create your views here.

def index(request, p=1, loj=None, cat=None, p_min=None, p_max=None):
    #Define as variáveis necessárias
    filters = {} #Dicionário com os filtros
    dicfilters = {} #Dicionário de filtros para enfeite do html
    loja = request.GET.get('loj', '')
    categoria = request.GET.get('cat', '')
    p_min = request.GET.get('p_min', 0)
    p_max = request.GET.get('p_max', 99999999999999999999)
    #Certifica que os preços são int e dentro do limite.
    try:
        p_min = int(p_min)
    except:
        p_min = 0
    try:
        p_max = int(p_max)
    except:
        p_max = 99999999999999999999
    if p_min < 0:
        p_min = 0
    if p_max > 99999999999999999999:
        p_max = 99999999999999999999
    #Começa a adicionar os filtros ao dicionário
    filters['preco__gte'] = p_min #sempre haverá valor mínimo
    dicfilters['p_min'] = p_min
    filters['preco__lte'] = p_max #sempre haverá valor máximo
    dicfilters['p_max'] = p_max
    if categoria != '': #se categoria tiver qlqr valor
        filters['produto__categoria'] = categoria #adiciona o filtro
        #tempvar = Produto.objects.get(categoria=categoria).values('categoria')
        #dicfilters['categoria'] = tempvar.nome_do_produto#
        #print(tempvar.nome_do_produto)
    if loja != '': #mesmo pra loja
        filters['loja__id'] = loja
        dicfilters['loja'] = Loja.objects.filter(id=loja).values('nome')
    #Query pro DB para buscar a lista de promoções:
    lista_de_promocoes = Promocao.objects.filter(**filters).order_by('-destaque', 'id') #Aplica os filtros
    #Lista de lojas para popular o select do filtro de busca:
    lista_de_lojas = Loja.objects.all()
    #Fornece o conteúdo do DB pro paginador do Django:
    paginador = Paginator(lista_de_promocoes, 9)
    #p = número da página, verificações seguintes impedem que seja negativo ou não inteiro.
    p = request.GET.get('p', 1)
    try:
        p = int(p)
    except:
        p = 1
    if p < 1:
        p = 1
    pagina = paginador.get_page(p)
    return render(request, 'promocoes/lista.html', { 'pagina': pagina, 'lista_de_lojas': lista_de_lojas, 'dicfilters': dicfilters })

def detail(request, id):
    promocao_em_destaque = get_object_or_404(Promocao, pk=id)
    return render(request, 'promocoes/detail.html', { 'promocao_em_destaque': promocao_em_destaque })

def edit(request, id):
    if request.method == 'GET':
        promocao_em_destaque = get_object_or_404(Promocao, pk=id)
        formulario = PromocaoEditForm(instance=promocao_em_destaque)
        return render(request, 'promocoes/edit.html', { 'promocao_em_destaque': promocao_em_destaque, 'formulario' : formulario })
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