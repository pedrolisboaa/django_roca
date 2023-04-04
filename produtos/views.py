from django.shortcuts import render
from .forms import AnuncioModelForm
from django.contrib import messages
from .models import  Anuncio

# Create your views here.

def index(request):
    
    conteudo  = {
        'anuncios': Anuncio.objects.all()
    }
    return render(request, 'index.html', conteudo)

def cadastro(request):
    
    if str(request.method) == 'POST':
        form = AnuncioModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Produto cadastro com sucesso.')
            
            form = AnuncioModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar o produto.')
    else:
        form = AnuncioModelForm()
            
  
    conteudo = {
        'form': form
    }    
    
    return render(request, 'cadastro.html', conteudo)

def contato(request):
    return render(request, 'contato.html')
