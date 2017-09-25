from django.contrib import admin
from agenda.models import Agenda
from agenda.models import UsuarioAgenda
from agenda.models import Usuario



admin.site.register(Agenda)
admin.site.register(Usuario)
admin.site.register(UsuarioAgenda)

# Register your models here.
