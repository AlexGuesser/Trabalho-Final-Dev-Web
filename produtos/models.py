from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.CharField(max_length=255) #link pra uma imagem
    descrição = models.TextField()
    categoria = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nome

    def nome_da_categoria(self):
        if self.categoria == 0:
            return "Hambúrguer de Carne"
        elif self.categoria == 1:
            return "Hambúrguer de Frango"
        elif self.categoria == 2:
            return "Acompanhamento"
        elif self.categoria == 3:
            return "Sobremesa"
        elif self.categoria == 4:
            return "Vegetariano"
        else:
            return "Categoria inválida"