from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Boleia

# Create your views here.

def home(request):
    template = loader.get_template('MyApp/index.html')
    return HttpResponse(template.render())

def boleias(request):
    # consulta a base de dados para obter as boleias
    boleias = Boleia.objects.all()

    # renderiza a página HTML com as boleias
    return render(request, 'index.html', {'boleias': boleias})
