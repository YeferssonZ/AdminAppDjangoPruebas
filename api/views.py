from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from dashboard.models import *
from .serializers import *
from rest_framework.decorators import action
# Create your views here.

class CuentaView(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnosSerializer

class ProfesorView(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesoresSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer

class AsistenciaView(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciasSerializer
    def get_queryset(self):
        queryset = Asistencia.objects.all()

        # Obtener el ID del alumno y el ID del curso desde los parámetros de la URL
        alumno_id = self.request.query_params.get('alumno', None)
        curso_id = self.request.query_params.get('curso', None)

        # Aplicar los filtros si se proporcionan los IDs del alumno y el curso
        if alumno_id and curso_id:
            queryset = queryset.filter(alumno=int(alumno_id), curso=int(curso_id))

        return queryset

class NotaView(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotasSerializer
    def get_queryset(self):
        queryset = Nota.objects.all()

        # Obtener el ID del alumno y el ID del curso desde los parámetros de la URL
        alumno_id = self.request.query_params.get('alumno', None)

        # Aplicar los filtros si se proporcionan los IDs del alumno y el curso
        if alumno_id:
            queryset = queryset.filter(alumno=alumno_id)

        return queryset
    

class InscripcionView(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionesSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        alumno_id = self.request.query_params.get('alumno')
        if alumno_id:
            queryset = queryset.filter(alumno=alumno_id)
        return queryset

class KeyAlumnoView(viewsets.ModelViewSet):
    queryset = KeyAlumno.objects.all()
    serializer_class = KeyAlumnosSerializer

class ObtenerInscripcionesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InscripcionesSerializer

    def get_queryset(self):
        alumno_id = self.kwargs['alumno_id']
        return Inscripcion.objects.filter(alumno=alumno_id)

class LaboratorioView(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    
class NotaByAlumnoAndCursoView(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotasSerializer

    def get_queryset(self):
        alumno_id = self.request.query_params.get('alumno')
        curso_id = self.request.query_params.get('curso')

        if alumno_id and curso_id:
            return Nota.objects.filter(alumno=alumno_id, curso=curso_id)

        return Nota.objects.none()

class CarreraView(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer