from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
#página inicial
def index(request):
    return render(request, 'index.html')


#página de contato
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!') 
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')   
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)



#página de cadastro de produtos
def produto(request):
    if str(request.method) == 'POST':	
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            messages.success(request, 'Produto salvo com sucesso!')
        else:
            messages.error(request, 'Erro ao salvar o produto.')

    return render(request, 'produto.html')