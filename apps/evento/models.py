""" Models Evento. """

# Django
from django.contrib.auth.models import User
from django.db import models
from . import choices
import uuid


def generate_config_id():
    return str(uuid.uuid4()).split("-")[-1]  # generate unique config id


# MODEL'S
class ConfigEvento(models.Model):
    id_config = models.CharField("ID", max_length=255, blank=True, editable=False)
    ver_disp = models.BooleanField("Verificador de Disponibilidad", default=False)
    ver_limit = models.BooleanField("Verificador de Limite", default=False)
    num_limit = models.IntegerField("Numero de asistentes", default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Configuracion de Evento"
        verbose_name_plural = "Configuraciones de Eventos"
        ordering = ['-created']

    def __str__(self):
        return "Configuración Nº {} - {}".format(self.id, self.id_config)

    def save(self, *args, **kwargs):
        if len(self.id_config.strip(" ")) == 0:
            self.id_config = generate_config_id()

        super(ConfigEvento, self).save(*args, **kwargs)  # Call the real save() method


class Evento(models.Model):
    """Modelo Evento - Represetan un evento realizado por DuocUC"""

    # DATABASE FIELDS
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=200)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    lugar = models.CharField('Lugar', max_length=200, null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=200, null=True, blank=True)
    ####
    sede = models.CharField('Sede organizadora', max_length=255, null=True, blank=True, choices=choices.CHOICES_SEDES,
                            default=choices.NP)
    escuela = models.CharField('Escuela organizadora', max_length=255, null=True, blank=True,
                               choices=choices.CHOICES_ESCUELA, default=choices.NP)
    area = models.CharField('Área organizadora', max_length=255, null=True, blank=True,
                            choices=choices.CHOICES_DIRECCION, default=choices.NP)
    ###
    fecha = models.DateField('Fecha del evento', null=True, blank=True)
    hora_inicio = models.TimeField('Hora de inico', null=True, blank=True)
    hora_fin = models.TimeField('Fecha de fin', null=True, blank=True)
    codigo = models.CharField('Codigo Evento', max_length=255, blank=True, null=True)
    usuario = models.ForeignKey(
        User,
        related_name='Eventos',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Usuario')
    config = models.ForeignKey(ConfigEvento, on_delete=models.CASCADE, blank=True,
        null=True, related_name="Evento", verbose_name="Configuracion")

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # META CLASS
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha']

    # TO STRING METHOD
    def __str__(self):
        return self.titulo

    # SAVE METHOD
    def save(self, *args, **kwargs):
        super(Evento, self).save(*args, **kwargs)
        numero_id = str(self.id)
        largo_titulo = str(len(self.titulo))
        titulo_split = self.titulo.split(" ")
        resul = numero_id + 'E' + largo_titulo + titulo_split[0]
        evento = Evento.objects.filter(id=self.id)
        evento.update(codigo=resul)


class Asistente(models.Model):
    """Modelo Asistente - Represetan un asistente a eventos"""

    # CHOICES
    ALD = 'Alumno Duoc UC'
    DD = 'Docente Duoc UC'
    AD = 'Administrativo Duoc UC'
    TD = 'Titulado Duoc UC'
    OE = 'Organizacion Empresarial'
    CL = 'Comunidad Local'
    OP = 'Organismo Publico'
    IE = 'Institucion de Educacion'
    OT = 'Otros'
    DEF = 'No especificado'

    CHOICES_GROUP = (
        (ALD, 'Alumno Duoc UC'),
        (DD, 'Docente Duoc UC'),
        (AD, 'Administrativo Duoc UC'),
        (TD, 'Titulado Duoc UC'),
        (OE, 'Organización Empresarial'),
        (CL, 'Comunidad Local'),
        (OP, 'Organismo Público'),
        (IE, 'Institución de Educación'),
        (OT, 'Otros'),
    )

    # DATABASE FIELDS
    identificador = models.CharField(max_length=12, verbose_name='Numero Identificador')
    nombre = models.CharField(max_length=256, verbose_name='Nombre', null=True, blank=True)
    apellido = models.CharField(max_length=256, verbose_name='Apellido', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Correo')
    telefono = models.BigIntegerField('Numero de Telefono', null=True, blank=True, default=0)
    grupo = models.CharField('Grupo al que pertenece', max_length=255, null=True, blank=True, choices=CHOICES_GROUP,
                             default=DEF)
    otro_grupo = models.CharField(max_length=256, null=True, blank=True, verbose_name='Otro grupo')

    validador = models.BooleanField(default=False, verbose_name='Estado acreditacion')
    evento = models.ForeignKey(
        Evento,
        verbose_name='Evento',
        related_name='Asistentes',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')

    # META CLASS
    class Meta:
        verbose_name = 'Asistente'
        verbose_name_plural = 'Asistentes'
        ordering = ['nombre', 'validador']

    # TO STRING METHOD
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
