from django.contrib import admin
from django import forms

from .models import *
# Register your models here.
from django import forms
from .models import Curso
'''
class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('alumnos',)

    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "alumnos":
            # Obtener el ciclo seleccionado en el formulario
            ciclo_id = request.POST.get('ciclo', None)
            if ciclo_id:
                # Filtrar los alumnos por el ciclo seleccionado
                kwargs["queryset"] = Alumno.objects.filter(ciclo_id=ciclo_id)
            else:
                # Mostrar todos los alumnos si no hay ciclo seleccionado
                kwargs["queryset"] = Alumno.objects.none()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

'''


admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Ciclo)
admin.site.register(Cuenta)
admin.site.register(Aula)
admin.site.register(Roles)
admin.site.register(Laboratorio)
admin.site.register(Nota)
admin.site.register(Inscripcion)
admin.site.register(Asistencia)
admin.site.register(KeyAlumno)
