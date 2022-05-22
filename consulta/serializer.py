from django.utils import timezone
from rest_framework import serializers

from agenda.models import Agenda, Horario
from consulta.models import Consulta
from medico.models import Medico
from medico.serializers import MedicoSerializer


class ReadConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horario = serializers.SerializerMethodField()

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')

    def get_horario(self, obj):
        return obj.horario.horario


class WriteConsultaSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def validate(self, attrs):
        try:
            agenda = Agenda.objects.all().get(id=attrs['agenda_id'])
        except Agenda.DoesNotExist:
            raise serializers.ValidationError("Agenda não encontrada")

        try:
            horario = Horario.objects.get(agenda=agenda, horario=attrs['horario'])
        except Horario.DoesNotExist:
            raise serializers.ValidationError("Horário não encontrado para agenda especificada")

        if agenda.dia < timezone.now().date():
            raise serializers.ValidationError("Não é possivel marcar uma consulta pra um dia passado")

        if agenda.dia == timezone.now().date() and horario.horario < timezone.now().time():
            raise serializers.ValidationError("Não é possivel marcar uma consulta pra um horário passado")

        exists = Consulta.objects.filter(
            agenda=agenda,
            horario=horario,
        ).count()

        if exists:
            raise serializers.ValidationError("Consulta para esta agenda / horário já foi marcada")

        return attrs

    def create(self, validated_data):
        agenda = Agenda.objects.get(id=validated_data['agenda_id'])
        horario = Horario.objects.get(agenda=agenda, horario=validated_data['horario'])
        medico = Medico.objects.get(id=agenda.medico.id)

        consulta = Consulta.objects.create(
            agenda=agenda,
            dia=agenda.dia,
            horario=horario,
            medico=medico
        )

        return consulta

    def to_representation(self, instance):
        return ReadConsultaSerializer(instance).data
