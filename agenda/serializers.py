from rest_framework import serializers
from django.core.serializers import json
from agenda.models import Agenda, Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        exclude = ('id', 'agenda')


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.SerializerMethodField()

    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'horarios', 'medico')
        depth = 1

    def get_horarios(self, obj):
        times = Horario.objects.filter(agenda=obj)
        times = HorarioSerializer(times, many=True)
        return times.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['horarios'] = map(lambda d: d['horario'], representation['horarios'])
        return representation



