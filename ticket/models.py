from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	
	descricao = models.CharField(max_length=200)
	
	def __unicode__(self):
   		return '%s' % (self.descricao) 


class Estado(models.Model):

	estado = models.CharField(max_length=200)
	
	def __unicode__(self):
   		return '%s' % (self.estado) 

class Ticket(models.Model):
	
	titulo = models.CharField(max_length=200)
	mensagem = models.CharField(max_length=200)
	anexo = models.FileField()
	categoria = models.ForeignKey(Categoria)
	estado = models.ForeignKey(Estado)
	user = models.ForeignKey(User)

	def __unicode__(self):
   		return '%s' % (self.titulo) 		