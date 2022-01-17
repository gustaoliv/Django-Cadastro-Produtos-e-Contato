from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
#página inicial
def index(request):
    return render(request, 'index.html')


#página de contato
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print("Mensagem enviada")

            messages.sucess(request, 'E-mail enviado com sucesso!') 
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')   
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)



#página de cadastro de produtos
def produto(request):
    return render(request, 'produto.html')