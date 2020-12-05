from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect #HttpResponse
from .forms import CadastroCustom, CadastroCustomEdit


# Create your views here.

def cadastrar(request):
    if request.method == 'POST' and not request.user.is_authenticated:
        erros = []
        formulario = CadastroCustom(request.POST)
        comparador = User.objects.filter(email=request.POST['email'])
        if comparador:
            erros.append('E-mail em uso. Tente recuperar sua senha.')
        if formulario.is_valid() and not erros:
            usuario = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password1'])
            usuario.save()
            grupo = Group.objects.get(name='Cliente')
            grupo.user_set.add(usuario)
            return render(request, 'usuarios/cadastro_sucesso.html', {  })
        else:
            return render(request, 'usuarios/cadastrar.html', { 'formulario': formulario, 'erros': erros })
    if request.method == 'GET':
        return render(request, 'usuarios/cadastrar.html', { 'formulario': CadastroCustom })

def perfil(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            formulario = CadastroCustomEdit(request.POST)
            if formulario.is_valid():
                usuario = User.objects.get(id=request.user.id)
                if request.POST['first_name']:
                    usuario.first_name = request.POST['first_name']
                if request.POST['last_name']:
                    usuario.last_name = request.POST['last_name']
                if request.POST['email']:
                    usuario.email = request.POST['email']
                if request.POST['password1']:
                    usuario.set_password(request.POST['password1'])
                usuario.save()
                erros = ['Alteração cadastral realizada com sucesso.']
                return render(request, 'usuarios/perfil.html', { 'formulario': formulario, 'erros': erros })
            else:
                return render(request, 'usuarios/perfil.html', { 'formulario': formulario })
        else:
            return HttpResponseRedirect('/usuarios/login/')
    if request.method == 'GET':
        if request.user.is_authenticated:
            usuario = get_object_or_404(User, pk=request.user.id)
            formulario = CadastroCustomEdit(instance=usuario)
            return render(request, 'usuarios/perfil.html', { 'formulario': formulario })
        else:
            return HttpResponseRedirect('/usuarios/login/')
