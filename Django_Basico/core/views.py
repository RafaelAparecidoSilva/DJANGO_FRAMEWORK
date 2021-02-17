from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    produtos = Produto.objects.all() #Pegar todos os nomes dos Produtos no Banco de Dados
    context = {
        'curso': 'Programação Web com Django Framework',
        'produto': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prods = Produto.objects.get(id=pk)
    prods = get_object_or_404(Produto, id=pk) #função de tratamento de erro
    context = {
        'prod': prods
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)