from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint

from agenda.models import Horario, Agenda
from medico.models import Medico


class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

