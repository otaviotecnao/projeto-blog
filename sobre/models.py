from django.db import models

class SobreNos(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    descricao = models.TextField(u'Descricao')
