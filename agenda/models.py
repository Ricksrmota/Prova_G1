from django.db import models

# Create your models here.

class Agenda(models.Model):
    compromisso = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    privado = models.BooleanField()
    institucional = models.BooleanField()

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    iduser = models.CharField(max_length=128,blank=False, null=False)
    nome = models.CharField(max_length=128,blank=False, null=False)

    def __str__(self):
        return self.nome

class UsuarioAgenda(models.Model):
    nome = models.ForeignKey(Usuario, null=True, blank=True, related_name='NomeUsuario')
    compromisso = models.ForeignKey(Agenda, null=True, blank=True, related_name='compromissoUsuario')
    convidados = models.ManyToManyField('Usuario')


