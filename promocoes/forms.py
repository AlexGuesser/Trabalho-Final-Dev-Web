from django import forms
from django.forms import ModelForm
from .models import Promocao

class PromocaoForm(ModelForm):
    class Meta:
        model = Promocao
        fields = '__all__'
        exclude = ['favoritos']
        widgets = {
            'produto': forms.Select(attrs={'class': 'browser-default'}),
            'loja': forms.Select(attrs={'class':'browser-default'}),
        }


class PromocaoEditForm(ModelForm):
    class Meta:
        model = Promocao
        exclude = ['produto', 'loja', 'favoritos']