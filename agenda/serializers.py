from rest_framework import serializers
from agenda.models import Agenda, Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        exclude = ['id']


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'horarios', 'medico')
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['horarios'] = map(lambda d: d['horario'], representation['horarios'])
        return representation
