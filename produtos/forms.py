from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    """
    nome = forms.CharField(label='Nome', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    uf  = forms.CharField(label='UF', max_length=2)
    email = forms.EmailField(label='E-mail', max_length=100)
    """
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = { 'categoria': forms.Select(attrs={'class': 'browser-default'}), }
        #fields = ['nome', 'cidade', 'uf', 'email'] -> Se quiser usar campos específicos.
        #exclude = ['title'] -> Se quiser excluir algum campo
        #widgets = {
            #'nome': forms.TextInput(attrs={'class': 'CSSVaiAqui'}),
        #}