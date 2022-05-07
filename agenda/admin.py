from django.contrib import admin

# Register your models here.

from agenda.forms import AtLeastOneRequiredInlineFormSet
from agenda.models import Agenda, Horario


class HorariosInline(admin.TabularInline):
    model = Horario
    formset = AtLeastOneRequiredInlineFormSet


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    inlines = [HorariosInline, ]

