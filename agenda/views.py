from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .filters import AgendaFilters
from .serializers import AgendaSerializer
from .models import Agenda

from consulta.models import Consulta

from django.utils import timezone
from django.db.models import Q


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_class = AgendaFilters
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        qs = Agenda.objects.filter(
            Q(dia__gte=timezone.now().date())
        )

        horarios = []

        for agenda in qs:
            if agenda.dia > timezone.now().date():
                for horario in agenda.horarios.all():
                    if Consulta.objects.filter(agenda=agenda, horario=horario).exists():
                        continue
                    else:
                        horarios.append(horario)

            if agenda.dia == timezone.now().date():
                for horario in agenda.horarios.filter(Q(horario__gt=timezone.now().time())):
                    if Consulta.objects.filter(agenda=agenda, horario=horario).exists():
                        continue
                    else:
                        horarios.append(horario)

            if len(horarios) > 0:
                agenda.horarios.set(horarios)
            else:
                qs = qs.exclude(pk=agenda.id)

        return qs
