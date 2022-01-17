from django.shortcuts import render


#página inicial
def index(request):
    return render(request, 'index.html')


#página de contato
def contato(request):
    return render(request, 'contato.html')


#página de cadastro de produtos
def produto(request):
    return render(request, 'produto.html')