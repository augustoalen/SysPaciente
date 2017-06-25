#coding: utf-8

from django.db import models

class DadosPessoais(models.Model):
	nome = models.CharField(max_length=50, verbose_name='Nome', default='')

	def __str__(self):
		return self.nome
