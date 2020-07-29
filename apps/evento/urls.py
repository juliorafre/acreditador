# Author = julioramirezdefreitas
# Created on : 12/23/18
# Mantainer = julioramirezdefreitas
# Email = julio157ramirez@gmail.com


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='principal'),
    path('eliminar-evento/<int:id_evento>', views.deleteEvent, name='eliminar_evento'),
    path('detalle-evento/<int:id_evento>', views.eventoDetail, name='detalle_evento'),
    path('acreditar-asistente/<int:id_evento>/<int:id_asistente>', views.UpdateAsistente, name='acreditar-asistentes'),
    path('acreditar-asistente-acreditadores/<int:id_evento>/<int:id_asistente>', views.UpdateAsistenteAcreditador, name='acreditar-asistentes-acreditadores'),
    path('acreditador-eventos/<str:codigo>', views.acreditacionEventoView, name='acreditador_eventos'),
    path('eliminar-asistente/<int:id_evento>/<int:id_asistente>', views.eliminarAsistente, name='eliminar_asistente'),
    path('desacreditar_asistente/<int:id_evento>/<int:id_asistente>', views.desacreditarAsistente, name='desacreditar_asistente'),
    path('actualizar-evento/<int:evento_pk>', views.updateEvento.as_view(), name='actualizar-evento'),
    path('gestion-usuarios', views.signup_view, name='gestion-usuario'),
    path('inscripcion-evento-duoc-uc/<int:id_evento>', views.eventoFormulario, name='formulario_inscripcion'),
    path('incripcion-finalizada-exitosa/<int_id_evento>', views.formularioConfirmation, name='formulario-exitoso'),
    path('configurar-disponibilidad/<int:id_evento>', views.cambiarDisponibilidad, name='cambiar-disponibilidad'),
    path('export/asistentes/xls/<int:id_evento>', views.export_asistentes_xls, name='export_users_xls'), #Excel
]
