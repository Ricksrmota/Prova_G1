from django.contrib import admin
from agenda.models import Agenda
from agenda.models import UsuarioAgenda
from agenda.models import Usuario
from agenda.models import Convidados



admin.site.register(Agenda)
admin.site.register(Usuario)
admin.site.register(UsuarioAgenda)
admin.site.register(Convidados)

# Register your models here.
