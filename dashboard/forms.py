from django.forms import ModelForm
from .models import *

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'


class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class CuentaForm(ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'ciclo', 'profesor', 'aulas']

