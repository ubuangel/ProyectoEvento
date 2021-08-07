from django.db import models
from equipo.models import Equipos
# Create your models here.

class Eventos(models.Model):
    event_cover_photo = models.ImageField(upload_to="event_cover/")
    eventonombre = models.CharField(blank=False, max_length = 255,unique=True)
    eventolugar = models.TextField(blank=False)
    descripcion = models.TextField(blank=False)
    inicio_fecha = models.DateTimeField()
    final_fecha = models.DateTimeField()
    creado_en = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    
    
class Detalles_par(models.Model):
    nombre = models.CharField(blank=False, max_length = 255)
    std_id = models.CharField(blank=False, max_length = 255)
    email = models.EmailField(blank=False,max_length=255)
    celular = models.CharField(blank=False, max_length = 255)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
