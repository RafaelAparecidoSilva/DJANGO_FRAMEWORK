from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin): #Classe para configurar o display do Admin
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


# Register your models here.
admin.site.register(Produto, ProdutoAdmin) #Chama a classe Produto e as configurações do admin
admin.site.register(Cliente, ClienteAdmin)