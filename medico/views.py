from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import MedicoSerializer
from .models import Medico


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all().order_by('nome')
    serializer_class = MedicoSerializer
