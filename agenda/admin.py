from django.contrib import admin
from agenda.models import Agenda
from agenda.models import AgendaPrivada
from agenda.models import AgendaInstituicao
from agenda.models import UsuarioAgenda
from agenda.models import Usuario
from agenda.models import UsuarioAgendaPrivada


admin.site.register(Agenda)
admin.site.register(AgendaPrivada)
admin.site.register(AgendaInstituicao)
admin.site.register(Usuario)
admin.site.register(UsuarioAgenda)
admin.site.register(UsuarioAgendaPrivada)
# Register your models here.
