from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Boleia
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.

def index(request):
    # consulta a base de dados para obter as boleias
    boleias = Boleia.objects.all()

    # renderiza a página HTML com as boleias e outros dados de contexto
    template = loader.get_template('MyApp/index.html')
    context = {'boleias': boleias}
    return HttpResponse(template.render(context, request))

def search(request):
    partida = request.GET.get('partida')
    chegada = request.GET.get('chegada')
    boleias = Boleia.objects.filter(partida__icontains=partida, chegada__icontains=chegada)
    #print(boleias)
    return render(request, 'MyApp/index.html', {'boleias': boleias})

def reset(request):
    boleias = Boleia.objects.all()
    return render(request, 'MyApp/index.html', {'boleias': boleias})

