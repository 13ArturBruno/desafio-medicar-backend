from django.contrib import admin
from consulta.models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False