from django.db import models
from cuentas.models import Cuentas
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Equipos(models.Model):
    nombre_equipo = models.CharField(blank=False, max_length = 255,unique=True)
    nombre_corto = models.CharField(blank=False, max_length = 10)
    emailequipo = models.EmailField(max_length=255,blank=True)
    password = models.CharField(max_length=255,blank=True)
    logo = models.ImageField(upload_to="equipo_logo/")
    descripcion = models.TextField(blank=False)
    form = models.DateField(auto_now_add=True)
    es_activo = models.BooleanField(default=True)
    ec = models.ManyToManyField(Cuentas, through='equipo_ec')


    def __str__(self):
        return self.nombre_equipo

class Equipo_Ec(models.Model):
    ec = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)
    designacion = models.CharField(max_length=64)

class Galeria(models.Model):
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="gallery/")
    fecha_subida = models.DateField(auto_now_add=True)


class miembro(models.Model):
    nombre = models.CharField(blank=False, max_length = 255)
    std_id = models.CharField(blank=False, max_length = 13)
    email = models.EmailField(max_length=255,blank=True)
    numero_celular = models.CharField(max_length = 15)
    semestre = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(21)])
    credito_completado = models.IntegerField(validators=[MinValueValidator(0)])
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)
