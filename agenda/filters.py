import django_filters
from django.core.exceptions import ValidationError
from django_filters import rest_framework as filters, fields
from django_filters.fields import DateRangeField
from django_filters.widgets import DateRangeWidget

from agenda.models import Agenda
from medico.models import Medico


# MUDANÇA DE SUFIXO
class CustomDateRangeWidget(DateRangeWidget):
    suffixes = ['inicio', 'final']


class CustomDateRangeField(DateRangeField):
    widget = CustomDateRangeWidget


class CustomDateRangeFilter(filters.DateFromToRangeFilter):
    field_class = CustomDateRangeField


# um oferecimento - Juninho
class CustomMultipleChoiceField(fields.ModelMultipleChoiceField):
    def _check_values(self, value):
        """
        Sobrescreve a classe base para que seja possivel filtar por pk
        que não exista, pois o comportamento padrão é retornar um
        bad request (400) enquanto o esperado é retornar um array vazio
        no caso de um filtro por uma chave inexistente
        """

        null = self.null_label is not None and value and self.null_value in value
        if null:
            value = [v for v in value if v != self.null_value]
        field_name = self.to_field_name or "pk"
        result = list(self.queryset.filter(**{"{}__in".format(field_name): value}))
        result += [self.null_value] if null else []
        return result

    def clean(self, value):

        value = self.prepare_value(value)

        # Caso onde não passou nenhum valor para a filtragem
        if not value:
            return self.queryset.all()

        if self.required and not value:
            raise ValidationError(self.error_messages["required"], code="required")
        elif not self.required and not value:
            return self.queryset.none()
        if not isinstance(value, (list, tuple)):
            raise ValidationError(
                self.error_messages["invalid_list"],
                code="invalid_list",
            )

        qs = self._check_values(value)
        # Since this overrides the inherited ModelChoiceField.clean
        # we run custom validators here
        self.run_validators(value)
        return qs


class CustomModelMultipleChoiceFilter(filters.ModelMultipleChoiceFilter):
    field_class = CustomMultipleChoiceField

    def filter(self, qs, value):
        if len(value) > 0:
            return super().filter(qs, value)

        return qs.none()


class AgendaFilters(django_filters.FilterSet):
    data = CustomDateRangeFilter(field_name='dia')

    medico = CustomModelMultipleChoiceFilter(
        field_name='medico',
        queryset=Medico.objects.all(),
    )

    crm = CustomModelMultipleChoiceFilter(
        field_name='medico__crm',
        to_field_name='crm',
        queryset=Medico.objects.all(),
    )

    class Meta:
        model = Agenda
        fields = ["medico", "crm", "dia"]
