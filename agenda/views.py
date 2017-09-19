from django.shortcuts import render
from agenda.models import Agenda
from agenda.models import AgendaInstituicao
from agenda.models import UsuarioAgenda
from django.http import HttpResponse

# Create your views here.


def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agenda.objects.all()
    for agenda in lista:
        retorno += '</br>Compromisso: {}</br>'.format(agenda.descricao) + '{}'.format(agenda.compromisso)
    return HttpResponse(retorno)

def listaAgendaFeriados(request):
    retorno = "<h1>Feriados</h1>"
    lista = AgendaInstituicao.objects.all()
    for agenda in lista:
        retorno += '</br>Data do Feriado: {}</br>'.format(agenda.compromisso)
    return HttpResponse(retorno)

def get_evento_byID(request,id):
    retorno = "<h1>Compromissos</h1>"
    agenda = UsuarioAgenda.objects.get(pk=id)
    retorno += '</br>Nome do Compromisso: {}</br>'.format(agenda.nome)
    return HttpResponse(retorno)