from django.contrib import admin
from .models import Evento, Asistente, ConfigEvento, Profile
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

admin.site.register(Profile)
admin.site.register(Evento)
admin.site.register(ConfigEvento)
admin.site.site_header = 'Administrador Acreditador'
admin.site.site_title = 'Administrador Acreditador'


class AsistenteResource(resources.ModelResource):
    class Meta:
        model = Asistente
        import_id_fields = ('identificador',)
        fields = ('identificador', 'nombre', 'apellido', 'email', 'telefono', 'grupo', 'validador', 'evento')
        exclude = ('created', 'updated',)

    def dehydrate_full_title(self, asistente):
        if  asistente:
            return  'Acreditado'
        else:
            return 'No acreditado'


@admin.register(Asistente)
class AsistenteAdmin(ImportExportActionModelAdmin):
    resource_class = AsistenteResource
    list_display = ('identificador', 'nombre','apellido', 'email', 'validador',)
    readonly_fields = ('created', 'updated',)
    list_filter = ('validador',)


