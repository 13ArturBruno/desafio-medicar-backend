# Create your views here.

from django.utils import timezone
from rest_framework import viewsets
from utils.mixins import MultiSerializerMixin
from .models import Consulta
from django.db.models import Q

from .serializer import WriteConsultaSerializer, ReadConsultaSerializer


class ConsultaViewSet(MultiSerializerMixin, viewsets.ModelViewSet):
    serializer_class = ReadConsultaSerializer
    serializer_action_map = {
        'create': WriteConsultaSerializer,
    }

    def get_queryset(self):
        qs = Consulta.objects.filter(
            Q(dia__gt=timezone.now().date()) |
            (Q(dia=timezone.now().date()) & Q(horario__horario__gt=timezone.now().time()))
        )
        return qs







