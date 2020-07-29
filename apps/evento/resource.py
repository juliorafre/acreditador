# Author = julioramirezdefreitas
# Created on : 1/2/19
# Mantainer = julioramirezdefreitas

from import_export import resources
from .models import Asistente


class AsistenteResource(resources.ModelResource):
    class Meta:
        model = Asistente
