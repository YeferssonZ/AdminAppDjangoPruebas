from django.db import models
from django.forms import ValidationError

from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_migrate



# Create your models here.
class Roles(models.Model):
    ADMIN = 'admin'
    ALUMNO = 'alumno'
    ROL_CHOICES = [
        (ADMIN, 'Admin'),
        (ALUMNO, 'Alumno')
    ]
    nombre = models.CharField(max_length=100, choices=ROL_CHOICES)
    def __str__(self):
        return self.nombre.capitalize()



class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Verificar si el objeto ya tiene un ID asignado
        if not self.id:
            # Obtener el máximo ID existente y agregar 1
            max_id = Cuenta.objects.aggregate(models.Max('id'))['id__max']
            self.id = max_id + 1 if max_id else 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='carreras/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    
class Ciclo(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    numero = models.IntegerField()
    def __str__(self):
        return f"Ciclo {self.numero} - {self.carrera.nombre}"

    class Meta:
        unique_together = ('carrera', 'numero')

    def clean(self):
        if self.numero < 1 or self.numero > 6:
            raise ValidationError("El número del ciclo debe estar entre 1 y 6.")




class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, null=True)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido
    

    

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.nombre + " " + self.apellido


class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    aulas = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre
    
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inscripción de {self.alumno} en {self.curso}"



class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.nombre} en {self.curso}"

class Asistencia(models.Model):
    ASISTIO = 'A'
    TARDANZA = 'T'
    FALTANTE = 'F'
    ESTADO_CHOICES = [
        (ASISTIO, 'Asistió'),
        (TARDANZA, 'Tardanza'),
        (FALTANTE, 'Faltante'),
    ]
    
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"Asistencia de {self.alumno} en {self.curso} el {self.fecha}: {self.get_estado_display()}"

class KeyAlumno(models.Model):
    clave = models.CharField(max_length=4, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self) :
        return f"Key de {self.alumno} es {self.clave}"




class Nota(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Nota de {self.alumno} en {self.laboratorio.nombre}"
    
   
@receiver(post_save, sender=Alumno)
def inscribir_alumno_en_cursos(sender, instance, created, **kwargs):
    if created and instance.ciclo:
        cursos_ciclo = Curso.objects.filter(ciclo=instance.ciclo)
        for curso in cursos_ciclo:
            Inscripcion.objects.create(alumno=instance, curso=curso)

@receiver(post_save, sender=Curso)
def inscribir_alumnos_en_curso(sender, instance, created, **kwargs):
    if created:
        alumnos_ciclo = Alumno.objects.filter(ciclo=instance.ciclo)
        for alumno in alumnos_ciclo:
            Inscripcion.objects.get_or_create(alumno=alumno, curso=instance)

@receiver(post_save, sender=Curso)
def crear_laboratorios(sender, instance, created, **kwargs):
    if created:
        for i in range(1, 17):
            Laboratorio.objects.create(nombre=f"Laboratorio {i}", curso=instance)


@receiver(post_save, sender=Alumno)
def crear_key_alumno(sender, instance, created, **kwargs):
    if created:
        KeyAlumno.objects.create(alumno=instance)

@receiver(post_migrate)
def asignar_claves_vacias(sender, **kwargs):
    if sender.name == 'dashboard':
        alumnos = Alumno.objects.all()
        for alumno in alumnos:
            KeyAlumno.objects.get_or_create(alumno=alumno)


from django.http import HttpResponse
from django.views import View

