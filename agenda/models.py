from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint
from django.utils import timezone

from medico.models import Medico


class Horario(models.Model):
    horario = models.TimeField(unique=True)

    class Meta:
        ordering = ['horario']

    def __str__(self):
        return str(self.horario)


class Agenda(models.Model):
    def validate_date(dia):
        if dia < timezone.now().date():
            raise ValidationError("Dia não pode ser no passado")

    medico = models.ForeignKey(Medico, related_name='medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[validate_date])
    horarios = models.ManyToManyField(Horario)

    class Meta:
        ordering = ['dia']
        constraints = [
            UniqueConstraint(fields=['medico', 'dia'],
                             name='unique_entry_agenda')
        ]

    def __str__(self):
        return self.medico.nome + ' / ' + str(self.dia)
