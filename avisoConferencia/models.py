from django.db import models
from cuentas.models import Cuentas

# Create your models here.
class Avisos(models.Model):
    avisotitulo = models.CharField(blank=False, max_length = 255,unique=True)
    descripcion = models.TextField(blank=False)
    creado_en = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.avisotitulo


class Noticias(models.Model):
    noticiatitulo = models.CharField(blank=False, max_length = 255,unique=True)
    descripcion = models.TextField(blank=False)
    creado_en = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.noticiatitulo
