# Author = julioramirezdefreitas
# Created on : 12/31/18
# Mantainer = julioramirezdefreitas


# Django
from django import forms


class EventAcrediForm(forms.Form):
    codigo = forms.CharField(
        label='Codigo de Evento',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo de evento'})
    )
