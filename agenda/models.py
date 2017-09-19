from django.db import models

# Create your models here.

class Agenda(models.Model):
    compromisso = models.DateField(blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao


class AgendaPrivada(Agenda):
    descricaoPrivada = models.TextField()

    def __str__(self):
        return self.descricao


class AgendaInstituicao(Agenda):
    feriados = models.CharField(max_length=128,blank=False, null=False)

class Usuario(models.Model):
    iduser = models.CharField(max_length=128,blank=False, null=False)
    nome = models.CharField(max_length=128,blank=False, null=False)

    def __str__(self):
        return self.nome

  

class UsuarioAgenda(models.Model):
    nome = models.ForeignKey(Usuario, null=True, blank=True)
    compromisso = models.ForeignKey(Agenda, null=True, blank=True)


class UsuarioAgendaPrivada(UsuarioAgenda):
    descricao = models.TextField()
