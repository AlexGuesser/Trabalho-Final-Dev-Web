from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = { 'categoria': forms.Select(attrs={'class': 'browser-default'}), }
