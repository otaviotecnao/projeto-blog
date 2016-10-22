from django.db import models

from redactor.fields import RedactorField

class SobreNos(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    descricao = RedactorField(u'Descricao')

    def __str__(self):
        return self.titulo
