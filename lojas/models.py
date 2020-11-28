from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome