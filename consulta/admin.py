from time import timezone

from django.contrib import admin

# Register your models here.
from consulta.models import Consulta

admin.site.register(Consulta)
