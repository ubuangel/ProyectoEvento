from django.db import models

# Create your models here.
class clendario_Academico(models.Model):
    calendario_label = models.CharField(blank=False,max_length = 255,unique=True)
    file = models.FileField(upload_to='academic_calendar/')
    subido_a = models.DateField(auto_now_add=True)
