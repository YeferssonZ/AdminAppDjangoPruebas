from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alumno, Curso, Inscripcion

@receiver(post_save, sender=Alumno)
def inscripcion_automatica(sender, instance, created, **kwargs):
    if created and instance.ciclo:
        ciclo = instance.ciclo
        cursos = Curso.objects.filter(ciclo=ciclo)
        for curso in cursos:
            Inscripcion.objects.create(alumno=instance, curso=curso)
