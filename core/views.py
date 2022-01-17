from django.shortcuts import render
from .forms import ContatoForm

#página inicial
def index(request):
    return render(request, 'index.html')


#página de contato
def contato(request):
    form = ContatoForm()
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


#página de cadastro de produtos
def produto(request):
    return render(request, 'produto.html')