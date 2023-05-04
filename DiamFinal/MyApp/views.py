from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Boleia

# Create your views here.

def index(request):
    # consulta a base de dados para obter as boleias
    boleias = Boleia.objects.all()

    # renderiza a página HTML com as boleias e outros dados de contexto
    template = loader.get_template('index.html')
    context = {'boleias': boleias}
    return HttpResponse(template.render(context, request))
