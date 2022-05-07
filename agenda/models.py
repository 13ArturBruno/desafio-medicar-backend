from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint
from django.utils import timezone

from medico.models import Medico


class Agenda(models.Model):
    def validate_date(dia):
        if dia < timezone.now().date():
            raise ValidationError("Dia não pode ser no passado")

    medico = models.ForeignKey(Medico, related_name='medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[validate_date])

    class Meta:
        constraints = [
            UniqueConstraint(fields=['medico', 'dia'],
                             name='unique_entry')
        ]

    def __str__(self):
        return self.medico.nome + ' / ' + str(self.dia)


class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()

    def __str__(self):
        return ''
