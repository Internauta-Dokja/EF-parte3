from django import forms
from .models import Zuñiga_Persona

class ZuñigaPersonaForm(forms.ModelForm):
    class Meta:
        model = Zuñiga_Persona
        fields = ['nombre', 'apellidos', 'sexo']