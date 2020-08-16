"""View Evento"""
# Author = julioramirezdefreitas
# Created on : 12/23/18
# Mantainer = julioramirezdefreitas
# Email = julio157ramirez@gmail.com

# Python
import datetime

# Django
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse  # Excel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from Acreditador.settings import URLWEB
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import xlwt  # Excel

# Resources
from .resource import AsistenteResource

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from .models import Evento, Asistente, ConfigEvento, Profile

# Forms
from .forms import EventoForm, Asistenteform, ConfigEventoForm, UserForm, ProfileForm


@login_required
def index(request):
    """Vista Inicial"""

    evento = Evento.objects.all()
    acreditadostotal = Asistente.objects.filter(validador=True)
    usuarios = User.objects.filter(is_staff=True, is_superuser=False)

    if request.user.username == 'Acreditador':
        logout(request)
        return redirect('login')

    user = request.user
    hoy_dia = datetime.date.today()
    eventos = Evento.objects.filter(usuario_id=user.id)
    eventoForm = EventoForm
    config_evento_form = ConfigEventoForm

    if 'crear_evento' in request.POST:
        print("La lista es: " + str(request.POST.getlist))

        if 'ver_limit' in request.POST:
            if request.POST['ver_limit'] == 'on':
                valueOfLimitValidation = True
        else:
            valueOfLimitValidation = False

        if 'num_limit' in request.POST:
            if int(request.POST['num_limit']) >= 0:
                valueOfNumOfPeople = request.POST['num_limit']
        else:
            valueOfNumOfPeople = 0

        ConfigEventoInstance = ConfigEvento.objects.create(
            ver_limit=valueOfLimitValidation,
            num_limit=valueOfNumOfPeople
        )

        try:
            Evento.objects.create(
                titulo=request.POST['titulo'],
                descripcion=request.POST['descripcion'],
                lugar=request.POST['lugar'],
                direccion=request.POST['direccion'],
                sede=request.POST['sede'],
                escuela=request.POST['escuela'],
                area=request.POST['area'],
                fecha=request.POST['fecha'],
                hora_inicio=request.POST['hora_inicio'],
                hora_fin=request.POST['hora_fin'],
                usuario=user,
                config=ConfigEventoInstance,
            )

            messages.success(request, 'Evento creado exitosamente.')
        except:
            messages.warning(request, 'Error al crear evento, intente de nuevo.')

    return render(
        request,
        'evento/index.html',
        {'eventos': eventos,
         'form_evento': eventoForm,
         'form_evento_config': config_evento_form,
         'fecha': hoy_dia,
         'evento': evento,
         'acredi': acreditadostotal,
         'usu': usuarios})


@login_required
def eventoDetail(request, id_evento):
    """Vista de detalle de evento"""
    evento = Evento.objects.get(id=id_evento)
    acreditados = evento.Asistentes.filter(validador=True).all()
    ausentes = evento.Asistentes.filter(validador=False).all()
    asistentes = Asistente.objects.filter(evento=evento).all()
    urlweb = URLWEB
    form_asistente = Asistenteform

    contexto = {
        'evento': evento,
        'acreditados': acreditados,
        'ausentes': ausentes,
        'form_asistente': form_asistente,
        'asistentes': asistentes,
        'urlweb': URLWEB
    }

    if 'agregar_asistente' in request.POST:
        if request.POST['identificador'] in asistentes.values_list('identificador', flat=True):
            messages.warning(request, 'El asistente ya se encuentra registrado')
            return render(request, 'evento/detail_evento.html', contexto)
        else:
            if 'on' in request.POST.getlist('validador'):
                resul = True
            else:
                resul = False

            asis = Asistente(
                identificador=request.POST['identificador'],
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                email=request.POST['email'],
                telefono=request.POST['telefono'],
                grupo=request.POST['grupo'],
                otro_grupo=request.POST['otro_grupo'],
                validador=resul,
            )
            asis.evento_id = id_evento
            try:
                asis.save()
                messages.success(request, 'El asistente ' + str(request.POST['identificador']) + '-' + str(
                    request.POST['nombre']) + ' ' + str(request.POST['apellido']) + ', se ha registrado con exito.')
            except:
                messages.warning(request, 'Problemas al registrar asistente.')

    return render(request, 'evento/detail_evento.html', contexto)


@login_required
def UpdateAsistente(request, id_evento, id_asistente):
    """Vista - Actualiza el estado de un asistente."""
    Asis = Asistente.objects.get(pk=id_asistente)
    Asis.validador = True
    try:
        Asis.save()
        messages.success(request, 'El asistente ha sido acreditado exitosamente')
    except:
        messages.warning(request, 'Error al acreditar asistente.')
    return redirect('detalle_evento', id_evento)


@login_required
def desacreditarAsistente(request, id_evento, id_asistente):
    """Vista - Actualiza el estado de un asistente."""
    Asis = Asistente.objects.get(pk=id_asistente)
    Asis.validador = False
    try:
        Asis.save()
        messages.success(request, 'El asistente ha sido desacreditado exitosamente')
    except:
        messages.warning(request, 'Error al desacreditar asistente.')
    return redirect('detalle_evento', id_evento)


@login_required
def eliminarAsistente(request, id_evento, id_asistente):
    """Vista - Actualiza el estado de un asistente."""
    Asis = Asistente.objects.get(pk=id_asistente)
    try:
        Asis.delete()
        messages.success(request, 'El asistente ha sido eliminado exitosamente')
    except:
        messages.warning(request, 'Error al eliminar asistente.')
    return redirect('detalle_evento', id_evento)


@login_required
def UpdateAsistenteAcreditador(request, id_evento, id_asistente):
    """Vista - Actualiza el estado de un asistente."""
    evento = Evento.objects.get(id=id_evento)
    Asis = Asistente.objects.get(pk=id_asistente)
    Asis.validador = True
    try:
        Asis.save()
        messages.success(request, 'El asistente ha sido acreditado exitosamente')
    except:
        messages.warning(request, 'Error al acreditar asistente.')
    return redirect('acreditador_eventos', evento.codigo.replace(' ', ''))


@method_decorator(login_required, name='dispatch')
class updateEvento(UpdateView):
    """Vista de actualizacion de evento"""
    template_name = 'evento/evento_update_form.html'
    model = Evento
    fields = ['titulo', 'descripcion', 'lugar', 'direccion', 'sede', 'escuela', 'area', 'fecha', 'hora_inicio',
              'hora_fin']
    context_object_name = "evento"
    pk_url_kwarg = 'evento_pk'
    success_url = reverse_lazy('principal')


@login_required
def deleteEvent(request, id_evento):
    """Vista - Elimina eventos."""
    evento = Evento.objects.get(pk=id_evento)
    try:
        evento.delete()
        messages.success(request, 'Evento eliminado con exito')
    except:
        messages.warning(request, 'Hubo problemas eliminando el evento.')
    return redirect('principal')


@login_required
def acreditacionEventoView(request, codigo):
    """Vista de acreditacion de Eventos DuocUC - Acreditadores"""
    evento = Evento.objects.get(codigo=codigo)
    acreditados = evento.Asistentes.filter(validador=True).all()
    ausentes = evento.Asistentes.filter(validador=False).all()
    asistentes = Asistente.objects.filter(evento=evento).all()
    form_asistente = Asistenteform

    contexto = {
        'evento': evento,
        'acreditados': acreditados,
        'ausentes': ausentes,
        'asistentes': asistentes,
        'form_asistente': form_asistente,
    }

    if datetime.date.today() > evento.fecha:
        return render(request, 'evento/descanso.html')

    if 'agregar_asistente' in request.POST:
        if request.POST['identificador'] in asistentes.values_list('identificador', flat=True):
            messages.warning(request, 'El asistente ya se encuentra inscrito')
            return render(request, 'evento/detail_evento_acreditador.html', contexto)
        else:
            if 'on' in request.POST.getlist('validador'):
                resul = True
            else:
                resul = False

            asis = Asistente(
                identificador=request.POST['identificador'],
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                email=request.POST['email'],
                telefono=request.POST['telefono'],
                grupo=request.POST['grupo'],
                otro_grupo=request.POST['otro_grupo'],
                validador=resul,
            )
            asis.evento_id = evento.id
            try:
                asis.save()
                messages.success(request, 'El asistente ' + str(request.POST['identificador']) + '-' + str(
                    request.POST['nombre']) + ' ' + str(request.POST['apellido']) + ', se ha registrado con exito.')
            except:
                messages.warning(request, 'Problemas al registrar asistente.')

    return render(request, 'evento/detail_evento_acreditador.html', contexto)


@login_required
@transaction.atomic
def signup_view(request):
    """Vista de creacion de usuarios administradores"""
    usuario = User.objects.filter(is_staff=True, is_superuser=False).all().select_related('profile')
    evento = Evento.objects.all()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            print("El nombre del usuario nuevo es: {}".format(profile_form.cleaned_data['area']))
            # user_form.save()
            # profile_form.save()

            user = User.objects.create(
                username=user_form.cleaned_data['username'],
                is_staff=True,
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
                email=user_form.cleaned_data['email'],
            )
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            user.profile.cargo = profile_form.cleaned_data['cargo']
            user.profile.area = profile_form.cleaned_data['area']
            user.profile.sede = profile_form.cleaned_data['sede']

            user.save()

            messages.success(request, 'Usuario creado exitosamente.')
        else:
            messages.warning(request, 'El usuario ya existe!')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    # if 'crear_usuario' in request.POST:
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     password_confirmation = request.POST['password_confirmation']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #
    #     if password != password_confirmation:
    #         messages.warning(request, 'Error en la confirmacion de contraseña. Intente de nuevo.')
    #         return render(request, 'evento/signup.html', {'usuarios': usuario})
    #
    #     try:
    #         user = User.objects.create(
    #             username=username,
    #             first_name=first_name,
    #             last_name=last_name,
    #             is_staff=True
    #         )
    #         user.set_password(password)
    #         user.save()
    #         messages.success(request, 'Usuario creado exitosamente.')
    #     except IntegrityError:
    #         messages.warning(request, 'El usuario ya existe!')
    # else:
    #     user_form = UserForm()
    #     profile_form = ProfileForm()

    return render(request, 'evento/signup.html',
                  {'usuarios': usuario, 'evento': evento, 'user_form': user_form, 'profile_form': profile_form})


def eventoFormulario(request, id_evento):
    """Vista de inscripcion a los eventos de DuocUC"""
    evento = Evento.objects.get(id=id_evento)
    asistentes = Asistente.objects.filter(evento=evento).all()
    form_asistente = Asistenteform

    contexto = {
        'evento': evento,
        'form_asistente': form_asistente,
        'asistentes': asistentes,

    }

    if datetime.date.today() > evento.fecha:
        return render(request, 'evento/formulario_evento_finalizado.html', {'evento': evento})

    if evento.config.ver_disp:
        return render(request, 'evento/formulario_evento_disable.html', {'evento': evento})

    if evento.config.ver_limit:
        if (asistentes.count() + 1) > evento.config.num_limit:
            return render(request, 'evento/vista_evento_completo.html', {'evento': evento})

    if 'inscribir_asistente' in request.POST:
        if request.POST['identificador'] in asistentes.values_list('identificador', flat=True):
            messages.warning(request, 'El asistente ya se encuentra inscrito')
            return render(request, 'evento/formularioInscripcion.html', contexto)
        else:
            asis = Asistente(
                identificador=request.POST['identificador'],
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                email=request.POST['email'],
                telefono=request.POST['telefono'],
                grupo=request.POST['grupo'],
                otro_grupo=request.POST['otro_grupo'],
            )
            asis.evento_id = id_evento
            try:
                asis.save()
                return render(request, 'evento/formulario_Confirmation_new.html',
                              {'evento': evento, 'id_evento': id_evento})
            except:
                messages.warning(request, 'Problemas al inscribirse. Intente de nuevo mas tarde')

    return render(request, 'evento/formularioInscripcion.html', contexto)


@login_required
def cambiarDisponibilidad(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    configuracion = ConfigEvento.objects.get(id_config=evento.config.id_config)
    estado = configuracion.ver_disp
    if estado:
        configuracion.ver_disp = False
    else:
        configuracion.ver_disp = True
    configuracion.save()
    return redirect('detalle_evento', id_evento)


def formularioConfirmation(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    return render(request, 'evento/formularioConfirmation.html', {'evento': evento, 'id_evento': id_evento})


# EXCEL

def export_asistentes_xls(request, id_evento):
    response = HttpResponse(content_type='application/ms-excel')

    evento = Evento.objects.get(id=id_evento)
    acreditados = evento.Asistentes.filter(validador=True).all()
    ausentes = evento.Asistentes.filter(validador=False).all()

    archivoNombre = "Resumen Asistentes_" + evento.titulo.replace(" ", "_") + ".xls"

    response['Content-Disposition'] = 'attachment; filename="' + archivoNombre + "\""

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Acreditados', cell_overwrite_ok=True)
    wsDos = wb.add_sheet('No Acreditados', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0
    rowDos_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Identificador', 'Nombre', 'Apellido', 'Email', 'Telefono', 'Grupo']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        wsDos.write(rowDos_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = evento.Asistentes.filter(validador=True).values_list('identificador', 'nombre', 'apellido', 'email',
                                                                'telefono', 'grupo', 'otro_grupo')

    rowsDos = evento.Asistentes.filter(validador=False).values_list('identificador', 'nombre', 'apellido', 'email',
                                                                    'telefono', 'grupo', 'otro_grupo')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    for row in rowsDos:
        rowDos_num += 1
        for col_num in range(len(row)):
            wsDos.write(rowDos_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_eventos_xls(request):
    """View export excel - Todos los Eventos."""

    evento = Evento.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Acreditados', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Identificador', 'Nombre', 'Lugar', 'Direccion', 'Fecha', 'Codigo']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Evento.objects.all().values_list('titulo', 'descripcion', 'lugar', 'direccion', 'fecha', 'codigo')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
