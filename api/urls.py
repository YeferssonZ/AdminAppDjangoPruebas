from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cuenta',views.CuentaView,basename="cuenta")
router.register(r'alumno',views.AlumnoView,basename="alumno")
router.register(r'curso',views.CursoView,basename="curso")
router.register(r'profesor',views.ProfesorView,basename="profesor")
router.register(r'inscripcion',views.InscripcionView,basename="inscripcion")
router.register(r'asistencia',views.AsistenciaView,basename="asistencia")
router.register(r'nota',views.NotaView,basename="nota")
router.register(r'keyAlumno',views.KeyAlumnoView,basename="keyAlumno")
router.register(r'laboratorio',views.LaboratorioView,basename="laboratorio")
router.register(r'inscripcion-alumno/(?P<alumno_id>\d+)', views.ObtenerInscripcionesViewSet, basename='obtener_inscripciones_alumno')
router.register(r'nota-by-alumno-curso', views.NotaByAlumnoAndCursoView, basename='nota_by_alumno_curso')
router.register(r'carrera',views.CarreraView,basename="carrera")
urlpatterns = [
    path('admin/',include(router.urls))
]