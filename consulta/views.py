# Create your views here.
from django.http import Http404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from utils.mixins import MultiSerializerMixin
from utils.trello import delete_card
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

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            try:
                delete_card(instance.trello_card_id)
            except:
                pass

            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
