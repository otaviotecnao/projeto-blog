from django.db import models

from redactor.fields import RedactorField

class SobreNos(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    descricao = RedactorField(u'Descricao')

    class Meta:
        verbose_name = 'Sobre nós'
        verbose_name_plural = 'Sobre nós'

    def __str__(self):
        return self.titulo
