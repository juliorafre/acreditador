""" Registrations Views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Models
from apps.evento.models import Evento

# Forms
from .forms import EventAcrediForm


# ----------------------------------------------------------------------- //


def login_view(request):
    """ Login view. """

    formAcreditacion = EventAcrediForm()

    if 'formAcreditacionEvento' in request.POST:
        codigo = request.POST.get('codigo', ' ')
        if Evento.objects.filter(codigo=codigo.replace(' ', '')).exists():
            return redirect('login_acreditador', codigo.replace(' ', ''))
        else:
            messages.warning(request, 'Acreditador: El evento no existe.')

    if 'iniciarSesion' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                login(request, user)
                return redirect('principal')
            except:
                messages.error(request, 'Error al iniciar sesion.')
        else:
            return render(request, 'registration/login.html', {'error': 'Nombre de usuario o contraseña invalido.'})

    return render(request, 'registration/login.html', {'formAcredi': formAcreditacion})


def loginAcreditador(request, codigo_evento):
    codigo = codigo_evento
    username = 'Acreditador'
    password = 'eventosDuocUC'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        try:
            login(request, user)
            return redirect('acreditador_eventos', codigo)
        except:
            messages.error(request, 'Error al iniciar sesion.')
    else:
        return redirect('login')


@login_required
def logout_view(request):
    """ Logout View."""
    logout(request)
    return redirect('login')


def eventoAcreditacion(request):
    """Vista para acreditar eventos"""
    codigoEventos = Evento.objects.values_list('codigo', flat=True)
    form = EventAcrediForm()
    if request.method == 'POST':
        form = EventAcrediForm(data=request.POST)
        if EventAcrediForm.is_valid():
            codigo = request.POST.get('codigo')
            if codigo in codigoEventos:
                return render(request)
