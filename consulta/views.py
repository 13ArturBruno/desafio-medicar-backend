from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response

from agenda.models import Agenda, Horario
from medico.models import Medico
from .models import Consulta
from .serializer import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        agenda = Agenda.objects.all().get(id=request.data.get('agenda_id'))
        horario = Horario.objects.get(agenda=agenda, horario=request.data.get('horario'))
        medico = Medico.objects.get(id=agenda.medico.id)

        consulta = Consulta.objects.create(
            agenda=agenda,
            dia=agenda.dia,
            horario=horario,
            medico=medico
        )

        serializer = self.get_serializer(consulta)
        return Response(serializer.data)




