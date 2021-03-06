from django.db import models
from medico.models import Medico, Consultorio
from tratamiento.models import Tratamiento
from catalogo.models import Estatus, Origen
from paciente.models import Paciente

# Create your models here.
class Cita (models.Model):
	hora_inicio=models.DateTimeField()
	hora_fin=models.DateTimeField()
	recomendaciones=models.CharField(max_length=500, null=True, blank=True)
	observaciones=models.CharField(max_length=500, null=True, blank=True)
	tratamiento=models.ForeignKey(Tratamiento, null=True, blank=True)
	consultorio=models.ForeignKey(Consultorio)
	estatus=models.ForeignKey(Estatus)
	medico=models.ForeignKey(Medico)
	paciente=models.ForeignKey(Paciente)
	origen=models.ForeignKey(Origen)

	def __unicode__(self):
		return u'%s - %s' % (self.hora_inicio, self.hora_fin)