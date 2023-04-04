from django import forms
from .models import Anuncio

# Com a base de dados

class AnuncioModelForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['nome', 'preco', 'contato', 'descricao', 'imagem']