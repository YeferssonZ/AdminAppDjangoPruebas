from django.test import TestCase
from django.forms import ValidationError
from .models import Roles, Cuenta, Carrera, Ciclo, Alumno, Profesor, Aula, Curso, Inscripcion, Laboratorio, Asistencia, KeyAlumno, Nota

class ModelTestCase(TestCase):
    def setUp(self):
        # Configurar objetos necesarios para las pruebas

        # Roles
        self.admin = Roles.objects.create(nombre='admin')
        self.alumno = Roles.objects.create(nombre='alumno')

        # Cuenta
        self.cuenta = Cuenta.objects.create(username='usuario', password='contraseña', rol=self.admin)

        # Carrera
        self.carrera = Carrera.objects.create(nombre='Ingeniería de Software')

        # Ciclo
        self.ciclo = Ciclo.objects.create(carrera=self.carrera, numero=1)

        # Alumno
        self.alumno = Alumno.objects.create(
            nombre='Juan',
            apellido='Pérez',
            email='juan@example.com',
            celular=123456789,
            ciclo=self.ciclo,
            cuenta=self.cuenta
        )

        # Profesor
        self.profesor = Profesor.objects.create(
            nombre='Pedro',
            apellido='Gómez',
            email='pedro@example.com',
            celular=987654321,
            cuenta=self.cuenta
        )

        # Aula
        self.aula = Aula.objects.create(nombre='Aula 101')

        # Curso
        self.curso = Curso.objects.create(
            nombre='Curso 101',
            ciclo=self.ciclo,
            profesor=self.profesor,
            aulas=self.aula
        )

    def test_roles_str_method(self):
        admin = Roles.objects.get(nombre='admin')
        alumno = Roles.objects.get(nombre='alumno')
        self.assertEqual(str(admin), 'Admin')
        self.assertEqual(str(alumno), 'Alumno')

    def test_ciclo_clean_method(self):
        # Prueba para verificar que la validación del método clean del modelo Ciclo funcione correctamente
        ciclo = Ciclo(carrera=self.carrera, numero=0)
        with self.assertRaises(ValidationError):
            ciclo.clean()

    def test_alumno_str_method(self):
        self.assertEqual(str(self.alumno), 'Juan Pérez')

    def test_curso_str_method(self):
        self.assertEqual(str(self.curso), 'Curso 101')

    def test_inscripcion_str_method(self):
        inscripcion = Inscripcion(alumno=self.alumno, curso=self.curso)
        self.assertEqual(str(inscripcion), 'Inscripción de Juan Pérez en Curso 101')

    def test_asistencia_str_method(self):
        asistencia = Asistencia(
            alumno=self.alumno,
            curso=self.curso,
            fecha='2023-01-01',
            estado=Asistencia.ASISTIO
        )
        self.assertEqual(str(asistencia), 'Asistencia de Juan Pérez en Curso 101 el 2023-01-01: Asistió')

    def test_key_alumno_str_method(self):
        key_alumno = KeyAlumno(clave='1234', alumno=self.alumno)
        self.assertEqual(str(key_alumno), 'Key de Juan Pérez es 1234')

    def test_nota_str_method(self):
        laboratorio = Laboratorio(nombre='Laboratorio 1', curso=self.curso)
        nota = Nota(laboratorio=laboratorio, alumno=self.alumno, nota=8.5)
        self.assertEqual(str(nota), 'Nota de Juan Pérez en Laboratorio 1')

