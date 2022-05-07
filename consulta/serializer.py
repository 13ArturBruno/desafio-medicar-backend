from rest_framework import serializers

from agenda.serializers import AgendaSerializer
from consulta.models import Consulta
from medico.serializers import MedicoSerializer


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horario = serializers.SerializerMethodField()

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')

    def get_horario(self, obj):
        return obj.horario.horario



