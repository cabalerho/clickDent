from django.contrib import admin
from direccion.models import *


class ColoniaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'cp', 'estado')

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('calle', 'colonia', 'num_exterior', 'num_interior')

admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(CP)
admin.site.register(Colonia, ColoniaAdmin)
admin.site.register(Direccion, DireccionAdmin)
