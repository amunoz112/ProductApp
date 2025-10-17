from django.shortcuts import render
from .models import Pedido

def index(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/index.html', {'pedidos': pedidos})
