from django.db import models
from agenda.models import Horario, Agenda
from medico.models import Medico


class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    trello_card_id = models.CharField(blank=True, max_length=300)

    class Meta:
        ordering = ['dia', 'horario__horario']

    def __str__(self):
        return self.medico.nome + ' / ' + str(self.dia) + ' / ' + str(self.horario.horario)


