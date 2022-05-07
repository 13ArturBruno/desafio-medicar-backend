from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import AgendaSerializer
from .models import Medico, Agenda


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all().order_by('medico__nome', 'dia')
    serializer_class = AgendaSerializer
