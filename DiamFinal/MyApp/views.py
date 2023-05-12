# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from .models import Boleia
# from django.http import JsonResponse
# from django.urls import reverse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from .forms import RegistrationForm
# from django.contrib.auth import logout
# from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Boleia
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .forms import BoleiaForm


from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

# def index(request):
#     # consulta a base de dados para obter as boleias
#     boleias = Boleia.objects.all()
#
#     # renderiza a página HTML com as boleias e outros dados de contexto
#     template = loader.get_template('MyApp/index.html')
#     context = {'boleias': boleias}
#     return HttpResponse(template.render(context, request))
#
# def search(request):
#     partida = request.GET.get('partida')
#     chegada = request.GET.get('chegada')
#
#     if partida and chegada:
#         # Filter Boleia objects using exact match on partida and chegada fields
#         boleias = Boleia.objects.filter(partida__iexact=partida, chegada__iexact=chegada)
#     else:
#         if partida:
#             boleias = Boleia.objects.filter(partida__iexact=partida)
#         else:
#             if chegada:
#                 boleias = Boleia.objects.filter(chegada__iexact=chegada)
#
#             else:
#                 # Fetch all Boleia objects
#                 boleias = Boleia.objects.all()
#
#     return render(request, 'MyApp/index.html', {'boleias': boleias})
#
#
# def reset(request):
#     boleias = Boleia.objects.all()
#     return render(request, 'MyApp/index.html', {'boleias': boleias})
#
# def about_view(request):
#     return render(request, 'MyApp/aboutUs.html')
#
# def information_view(request):
#     return render(request, 'MyApp/information.html')
#
# def anunciar_view(request):
#     return render(request, 'MyApp/anunciar.html')
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('MyApp:index'))
#         else:
#             return render(request, 'MyApp/login.html', {'error_message': 'Invalid login credentials'})
#     else:
#         return render(request, 'MyApp/login.html')
#
#
# # Register View
# def register_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             car_brand = form.cleaned_data.get('car_brand')
#             car_model = form.cleaned_data.get('car_model')
#             if form.is_valid():
#                 form.save()
#     else:
#         form = RegistrationForm()
#     return render(request, 'MyApp/register.html', {'form': form})


#@login_required(login_url='/MyApp/login')
def index(request):
    boleias = Boleia.objects.all()
    template = loader.get_template('MyApp/index.html')
    context = {'boleias': boleias}
    return render(request, 'MyApp/index.html', context)


def search(request):
    partida = request.GET.get('partida')
    chegada = request.GET.get('chegada')

    if partida and chegada:
        # Filter Boleia objects using exact match on partida and chegada fields
        boleias = Boleia.objects.filter(partida__iexact=partida, chegada__iexact=chegada)
    else:
        if partida:
            boleias = Boleia.objects.filter(partida__iexact=partida)
        else:
            if chegada:
                boleias = Boleia.objects.filter(chegada__iexact=chegada)

            else:
                # Fetch all Boleia objects
                boleias = Boleia.objects.all()

    return render(request, 'MyApp/index.html', {'boleias': boleias})


def reset(request):
    boleias = Boleia.objects.all()
    return render(request, 'MyApp/index.html', {'boleias': boleias})


def about_view(request):
    return render(request, 'MyApp/aboutUs.html')


def information_view(request):
    return render(request, 'MyApp/information.html')


def anunciar_view(request):
    if request.method == 'POST':
        form = BoleiaForm(request.POST)
        if form.is_valid():
            partida = form.cleaned_data['partida']
            chegada = form.cleaned_data['chegada']
            horario = form.cleaned_data['horario']
            preco = form.cleaned_data['preco']
            vagas = form.cleaned_data['vagas']
            detalhes = form.cleaned_data['detalhes']
            nova_boleia = Boleia(partida=partida, chegada=chegada, horario=horario, preco=preco, vagas=vagas, detalhes=detalhes)
            nova_boleia.motorista = request.user
            nova_boleia.save()
            return HttpResponseRedirect(reverse('MyApp:index'))
    else:
        form = BoleiaForm()
    return render(request, 'MyApp/anunciar.html', {'form': form})

def detalhes(request, boleia_id):
    boleia = get_object_or_404(Boleia, pk=boleia_id)
    if request.method == 'POST':
        boleia.vagas -= 1
        boleia.users.add(request.user)
        boleia.save()
        return HttpResponseRedirect(reverse('MyApp:detalhes', args=(boleia_id,)))
    return render(request, 'MyApp/detalhe.html', {'boleia': boleia})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('MyApp:index'))
        else:
            return render(request, 'MyApp/login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'MyApp/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('MyApp:login'))

# Register View
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            car_brand = form.cleaned_data.get('car_brand')
            car_model = form.cleaned_data.get('car_model')
            if form.is_valid():
                form.save()
    else:
        form = RegistrationForm()
    return render(request, 'MyApp/register.html', {'form': form})

# def user_info_view(request):
#     user = request.user
#     user_boleias = Boleia.objects.filter(users=user)
#     motorista = Boleia.objects.filter(motorista=user)
#     context = {
#         'user': user,
#         'boleias': user_boleias,
#         'motorista':motorista
#     }
#     return render(request, 'MyApp/user_info.html', context)

def user_info_view(request):
    user = request.user
    user_boleias = Boleia.objects.filter(users=user)
    motoristas = Boleia.objects.filter(motorista=user)
    context = {
        'user': user,
        'boleias': user_boleias,
        'motoristas':motoristas
    }

    return render(request, 'MyApp/user_info.html',context)
