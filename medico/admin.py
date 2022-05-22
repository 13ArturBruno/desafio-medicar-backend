from django.contrib import admin
from django.contrib.auth.models import User, Group
from medico.models import Medico

admin.site.register(Medico)

admin.site.unregister(User)
admin.site.unregister(Group)

