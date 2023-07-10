from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from dashboard.forms import AlumnoForm,ProfesorForm
from .models import *
from .forms import *
from django.http.response import JsonResponse
from django_dyn_dt.datatb import DataTB
from django.shortcuts import render
from .models import Carrera
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from django.db.models import Avg

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def BASE(request):
    return render(request, 'home.html')

def opcion(request):
    return render(request,'opcionAlumno.html' )

def index(request):
    return render (request, 'tblAlumno.html')
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = Alumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'tblAlumno.html',context)
    def post(self, request, pk = None):
        
    
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/listaAlumno')



def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    alumno.delete()
    return redirect('listalumno')


def modificar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)

    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listalumno')
    else:
        form = AlumnoForm(instance=alumno)

    return render(request, 'modificar_alumno.html', {'form': form, 'alumno': alumno})

class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = Profesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'tblProfesor.html',context)

def nuevo_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listprofesor')
    else:
        form = ProfesorForm()
    return render(request, 'nuevo_profesor.html', {'form': form})

def eliminar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    profesor.delete()
    return redirect('listprofesor')

def modificar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listprofesor')
    else:
        form = ProfesorForm(instance=profesor)
    
    return render(request, 'modificar_profesor.html', {'form': form, 'profesor': profesor})

class CursoView(View):
    
    def get(self,request):
        listaCursos = Curso.objects.all()
        formCurso = CursoForm()
        context = {
            'cursos' : listaCursos,
            'formCurso': formCurso
        }
        return render(request,'tblCurso.html',context)


class CuentaView(View):
    
    def get(self,request):
        listaCuentas = Cuenta.objects.all()
        formCuenta = CuentaForm()
        context = {
            'cuentas' : listaCuentas,
            'formCuenta': formCuenta
        }
        return render(request,'tblCuenta.html',context)
    
def nueva_cuenta(request):
    roles = Roles.objects.all()  # Obtener todos los roles de la base de datos

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rol_id = request.POST['rol']  # Obtener el ID del rol seleccionado

        # Obtener la instancia de Roles correspondiente al ID seleccionado
        rol = Roles.objects.get(id=rol_id)

        # Crear una nueva instancia de Cuenta con los datos recibidos
        cuenta = Cuenta(username=username, password=password, rol=rol)
        cuenta.save()

        return redirect('listcuenta')
    else:
        return render(request, 'nueva_cuenta.html', {'roles': roles})

def eliminar_cuenta(request, cuenta_id):
    cuenta = Cuenta.objects.get(id=cuenta_id)
    cuenta.delete()
    return redirect('listcuenta')

def modificar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    roles = Roles.objects.all()  # Obtener todos los roles

    if request.method == 'POST':
        # Se recibió una solicitud POST, se procesa el formulario de modificación

        # Obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        rol_id = request.POST['rol']

        # Obtener la instancia del modelo Roles correspondiente al ID recibido
        rol = get_object_or_404(Roles, id=rol_id)

        # Actualizar los atributos de la cuenta con los nuevos valores
        cuenta.username = username
        cuenta.password = password
        cuenta.rol = rol

        # Guardar los cambios en la base de datos
        cuenta.save()

        # Redirigir a la página de listado de cuentas o mostrar un mensaje de éxito
        return redirect('listcuenta')

    return render(request, 'modificar_cuenta.html', {'cuenta': cuenta, 'roles': roles})

class NuevoCursoView(View):
    def get(self, request):
        form = CursoForm()
        return render(request, 'nuevo_curso.html', {'form': form})
    
    def post(self, request):
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect('listcurso')  # Redirige a la lista de cursos después de crear uno nuevo
        return render(request, 'nuevo_curso.html', {'form': form})




def eliminar_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('listcurso')

from django.shortcuts import render, get_object_or_404
from .models import Curso


def modificar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':

        nombre = request.POST['nombre']
        ciclo = request.POST['ciclo']
        profesor = request.POST['profesor']
        aulas = request.POST['aulas']

        curso.nombre = nombre
        curso.ciclo = ciclo
        curso.profesor = profesor
        curso.aulas = aulas

        curso.save()

        return redirect('listcurso')
    
    return render(request, 'modificar_curso.html', {'curso': curso})


def alumnos_por_curso(request):
    cursos = Curso.objects.all()  
    contexto = {'cursos': cursos}  
    return render(request, 'alumnos_por_curso.html', contexto)

def lista_carreras(request):
    carreras = Carrera.objects.all()  
    contexto = {'carreras': carreras}  
    return render(request, 'carreras.html', contexto)


def inscritos_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    inscritos = curso.alumnos.all()

    context = {
        'curso': curso,
        'inscritos': inscritos
    }

    return render(request, 'tblAlumnoCurso.html', context)

'''
def laboratorios_alumno(request, curso_id, alumno_id):
    curso = Curso.objects.get(id=curso_id)
    alumno = Alumno.objects.get(id=alumno_id)
    laboratorios = Laboratorio.objects.filter(curso=curso)
    notas = Nota.objects.filter(alumno=alumno, laboratorio__in=laboratorios)

    # Crear un diccionario para almacenar las notas por laboratorio
    notas_laboratorios = {}
    for nota in notas:
        notas_laboratorios[nota.laboratorio] = nota.nota

    context = {
        'curso': curso,
        'alumno': alumno,
        'laboratorios': laboratorios,
        'laboratorios': laboratorios,
        'notas_laboratorios': notas_laboratorios,
    }

    return render(request, 'notas.html', context)
'''


def notas_alumno(request, curso_id, alumno_id):
    curso = Curso.objects.get(id=curso_id)
    alumno = Alumno.objects.get(id=alumno_id)
    laboratorios = Laboratorio.objects.filter(curso=curso)
    notas_laboratorios = Nota.objects.filter(laboratorio__in=laboratorios, alumno=alumno)

    context = {
        'curso': curso,
        'alumno': alumno,
        'notas_laboratorios': notas_laboratorios,
    }

    return render(request, 'notas.html', context)


def salir(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render
from .models import Asistencia

def mostrar_asistencias(request, curso_id):
    # Obtener el curso
    curso = Curso.objects.get(id=curso_id)
    # Obtener los alumnos inscritos en el curso
    alumnos = Alumno.objects.filter(inscripcion__curso=curso)

    # Obtener las asistencias de los alumnos en el curso
    asistencias = Asistencia.objects.filter(curso=curso)

    return render(request, 'tblAsistencia.html', {
        'curso': curso,
        'alumnos': alumnos,
        'asistencias': asistencias,
    })

def mostrar_inscritos(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    inscritos = Inscripcion.objects.filter(curso=curso)
    return render(request, 'tblInscritos.html', {'curso': curso, 'inscritos': inscritos})

def mostrar_notas(request, curso_id, alumno_id):
    # Obtener el curso y el alumno
    curso = Curso.objects.get(id=curso_id)
    alumno = Alumno.objects.get(id=alumno_id)

    # Obtener los laboratorios del curso
    laboratorios = Laboratorio.objects.filter(curso=curso)

    # Obtener las notas del alumno en los laboratorios del curso
    notas = Nota.objects.filter(alumno=alumno, laboratorio__curso=curso)

    # Calcular el promedio de las notas del alumno en los laboratorios
    promedio_notas = notas.aggregate(promedio=Avg('nota')).get('promedio')

    return render(request, 'notas.html', {
        'curso': curso,
        'alumno': alumno,
        'laboratorios': laboratorios,
        'notas': notas,
        'promedio_notas': promedio_notas,
    })