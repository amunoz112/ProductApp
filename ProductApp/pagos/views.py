from django.shortcuts import render
from .models import Pago

def index(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/index.html', {'pagos': pagos})
