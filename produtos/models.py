from django.db import models

# Create your models here.

class Produto(models.Model):
    CATEGORIAS_DISPONIVEIS = (
        ("0", "Hambúrguer de Carne"),
        ("1", "Hambúrguer de Frango"),
        ("2", "Acompanhamento"),
        ("3", "Sobremesa"),
        ("4", "Vegetariano"),
    )
    nome = models.CharField(max_length=200)
    imagem = models.CharField(max_length=255) #link pra uma imagem
    descrição = models.TextField()
    categoria = models.CharField(max_length=4, choices=CATEGORIAS_DISPONIVEIS)

    def __str__(self):
        return self.nome

    def nome_da_categoria(self):
        return dict(Produto.CATEGORIAS_DISPONIVEIS)[self.categoria]