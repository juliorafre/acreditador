
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #Path de Auth
    path('iniciar-sesion', views.login_view, name='login'),
    path('cerrar-sesion', views.logout_view, name='logout'),
    path('iniciar-sesion-acreditador/<str:codigo_evento>', views.loginAcreditador, name='login_acreditador')
]
