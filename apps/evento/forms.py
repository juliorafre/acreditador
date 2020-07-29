# Author = julioramirezdefreitas
# Created on : 12/24/18
# Mantainer = julioramirezdefreitas

# Django
from django import forms

# Models
from .models import Evento, Asistente, ConfigEvento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'lugar', 'direccion', 'sede',
                  'escuela', 'area', 'fecha', 'hora_inicio', 'hora_fin', 'usuario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '5',
                                                 'placeholder': 'Breve descripcion del proposito del evento.',
                                                 'required': 'true'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'sede': forms.Select(attrs={'class': 'form-control'}),
            'escuela': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'required': 'true', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'required': 'true'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'required': 'true'}),
            'usuario': forms.HiddenInput(),
        }


class ConfigEventoForm(forms.ModelForm):
    class Meta:
        model = ConfigEvento
        fields = ['ver_limit', 'num_limit']
        widgets = {
            'ver_limit': forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'customCheck1'}),
            'num_limit': forms.TextInput(),
        }


class Asistenteform(forms.ModelForm):
    # Required eliminados Importante agregar en un futuro
    class Meta:
        model = Asistente
        fields = ['identificador', 'nombre', 'apellido', 'email',
                  'telefono', 'grupo', 'otro_grupo', 'validador', 'evento']
        widgets = {
            'identificador': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'true', 'placeholder': '11111111-1',
                       'pattern': '\d{7,8}-[0-9kK]'}),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': 'true',
                       'pattern': '[a-zA-ZñÑáéíóúÁÉÍÓÚ ]{1,255}'}),
            'apellido': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Apellido', 'pattern': '[a-zA-ZñÑáéíóúÁÉÍÓÚ ]{1,255}'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo', 'required': 'true'}),
            'telefono': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Telefono', 'pattern': '\d{9}'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'otro_grupo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Especifique grupo',
                       'pattern': '[0-9a-zA-ZñÑáéíóúÁÉÍÓÚ ]{1,255}'}),
            # 'validador': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'evento': forms.HiddenInput()
        }
