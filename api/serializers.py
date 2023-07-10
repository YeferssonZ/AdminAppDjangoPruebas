from rest_framework import serializers,generics
from dashboard.models import *

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class InscripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class AsistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        
class NotaByAlumnoAndCursoView(generics.ListAPIView):
    serializer_class = NotasSerializer

    def get_queryset(self):
        alumno_id = self.request.query_params.get('alumno')
        curso_id = self.kwargs['curso_id']

        queryset = Nota.objects.filter(alumno=alumno_id, laboratorio__curso=curso_id)
        return queryset
    
class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class KeyAlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyAlumno
        fields = '__all__'


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'