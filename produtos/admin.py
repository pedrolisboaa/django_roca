from django.contrib import admin
from .models import Anuncio
# Register your models here.

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'criado', 'contato', 'descricao')


