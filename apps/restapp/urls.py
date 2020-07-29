from django.conf.urls import url, include
# from django.contrib.auth.models import User
from ..evento.models import Asistente
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.

class AsistenteSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='fields-detail',)
    class Meta:
        model = Asistente
        fields = ['identificador', 'nombre', 'apellido', 'email', 'telefono', 'grupo', 'otro_grupo', 'validador',
                  'evento']


# ViewSets define the view behavior.
class AsistenteViewSet(viewsets.ModelViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'Asistentes', AsistenteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#
# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views
#
# urlpatterns = [
#     #Path de Auth
#     path('iniciar-sesion', views.login_view, name='login'),
#     path('cerrar-sesion', views.logout_view, name='logout'),
#     path('iniciar-sesion-acreditador/<str:codigo_evento>', views.loginAcreditador, name='login_acreditador')
# ]
