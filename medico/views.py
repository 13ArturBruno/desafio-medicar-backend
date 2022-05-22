from rest_framework import viewsets

from .serializers import MedicoSerializer
from .models import Medico


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
