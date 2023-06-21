from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render

from .models import cita

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name= "paladweb/profile_form.html"

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def cita(request):
    return render(request, 'cita.html', {})


def CREAR(request):
    return render(request, 'CREAR.html', {})

def ELIMINAR(request):
    return render(request, 'ELIMINAR.html', {})

def EDITAR(request):
    return render(request, 'EDITAR.html', {})

def PV(request):
    return render(request, 'PV.html', {})


def login(request):
    return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html', {})
