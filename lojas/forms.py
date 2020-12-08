from django import forms
from django.forms import ModelForm
from .models import Loja

class LojaForm(ModelForm):

    class Meta:
        model = Loja
        fields = '__all__'