from promocoes.models import Promocao
from produtos.models import Produto
from lojas.models import Loja
from rest_framework import serializers


class ProdutoSerializer (serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'imagem', 'descrição', 'categoria']


class LojaSerializer (serializers.ModelSerializer):

    class Meta:
        model = Loja
        fields = ['id', 'nome', 'cidade', 'uf', 'email']


class PromocaoSerializer (serializers.ModelSerializer):

    produto = serializers.SlugRelatedField(
        many=False,  read_only=False, queryset=Produto.objects.all(), slug_field='nome')
    loja = serializers.SlugRelatedField(
        many=False,  read_only=False, queryset=Loja.objects.all(), slug_field='nome')

    class Meta:
        model = Promocao
        fields = ['id', 'produto', 'loja', 'preco',
                  'cupom', 'destaque', 'favoritos']
