from django.contrib import admin

from models import *

class FromacionAdmin(admin.ModelAdmin):
	list_display = ('escuela', 'titulo', 'medico')

class ConsultorioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'medico')

class MedicoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'ape_paterno', 'ape_materno', 'num_cedula', 'declaracion', 'usuario', 'especialidad')

admin.site.register(Formacion, FromacionAdmin)
admin.site.register(Consultorio, ConsultorioAdmin)
admin.site.register(Medico, MedicoAdmin)
