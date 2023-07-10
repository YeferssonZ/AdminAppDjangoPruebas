from django.contrib import admin
from django.urls import path
from . import views
from .views import NuevoCursoView, alumnos_por_curso, eliminar_curso
from .views import lista_carreras


urlpatterns = [
    path('', views.BASE, name = 'BASE'),
    path('opcionAlumno/', views.opcion, name = 'opcion'),
    path('listaAlumno/', views.AlumnoView.as_view(),name='listalumno'),
    path('eliminar_alumno/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('alumnos/modificar/<int:alumno_id>/', views.modificar_alumno, name='modificar_alumno'),
    path('listaProfesor/', views.ProfesorView.as_view(),name='listprofesor'),
    path('profesores/nuevo/', views.nuevo_profesor, name='nuevo_profesor'),
    path('profesores/eliminar/<int:profesor_id>/', views.eliminar_profesor, name='eliminar_profesor'),
    path('profesores/<int:profesor_id>/modificar/', views.modificar_profesor, name='modificar_profesor'),
    path('listaCurso/', views.CursoView.as_view(),name='listcurso'),
    path('nuevo_curso/', NuevoCursoView.as_view(), name='nuevo_curso'),
    path('eliminar_curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),
    path('cursos/<int:curso_id>/modificar/', views.modificar_curso, name='modificar_curso'),
    path('curso/<int:curso_id>/inscritos/', views.mostrar_inscritos, name='mostrar_inscritos'),
    path('listaCuenta/', views.CuentaView.as_view(),name='listcuenta'),
    path('nueva_cuenta/', views.nueva_cuenta, name='nueva_cuenta'),
    path('eliminar_cuenta/<int:cuenta_id>/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('cuentas/<int:cuenta_id>/modificar/', views.modificar_cuenta, name='modificar_cuenta'),
    path('alumnos_por_curso/', alumnos_por_curso, name='alumnos_por_curso'),
    path('lista_carreras/', lista_carreras, name='lista_carreras'),
    path('inscritos/<int:curso_id>/', views.inscritos_curso, name='inscritos_curso'),
    #path('notas/<int:alumno_id>/<int:curso_id>/', views.notas_alumno_curso, name='notas_alumno_curso'),
    #path('notas/', NotasListView.as_view(), name='notas_list'),
    path('mostrar-notas/<int:curso_id>/<int:alumno_id>/', views.mostrar_notas, name='mostrar_notas'),
    path('mostrar_asistencias/<int:curso_id>/', views.mostrar_asistencias, name='mostrar_asistencias'),
    path('salir/', views.salir , name='salir')
    
]
