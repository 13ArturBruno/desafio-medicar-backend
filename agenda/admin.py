from django.contrib import admin
from agenda.models import Agenda, Horario


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    filter_horizontal = ['horarios']


admin.site.register(Horario)
