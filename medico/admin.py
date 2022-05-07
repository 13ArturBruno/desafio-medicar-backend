from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from medico.models import Medico

admin.site.register(Medico)

admin.site.unregister(User)
admin.site.unregister(Group)

