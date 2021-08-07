from django.db import models
from django import forms
#from phone_field import PhoneField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Admin_cuentas(BaseUserManager):
    def crear_usuario(self, email, nombreusuario, password=None):
        """
        Crea y guarda un Usuario con el correo electrónico, fecha de nacimiento y contraseña dados.
        """
        if not email:
            raise ValueError('Los usuarios deben tener una dirección de correo electrónico')
        if not nombreusuario:
            raise ValueError('Los usuarios deben tener un nombre de usuario.')

        user = self.model(
            email=self.normalize_email(email),
            nombreusuario=nombreusuario,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombreusuario, password=None):
        """
        Crea y guarda un superusuario con el correo electrónico dado, fecha de
         nacimiento y contraseña.
        """
        user = self.crear_usuario(
            email=email,
            password=password,
            nombreusuario=nombreusuario,
        )
        user.es_superusuario = True
        user.save(using=self._db)
        return user


class Cuentas(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nombreusuario = models.CharField(max_length = 20)
    imagen = models.ImageField(upload_to="Cuentas/")
    numero_celular = models.CharField(max_length = 15)
    nombrecompleto = models.CharField(max_length = 50)
    es_activo = models.BooleanField(default=True)
    es_admin = models.BooleanField(default=False)
    es_superusuario = models.BooleanField(default=False)
    is_ec = models.BooleanField(default=False)

    objects = Admin_cuentas()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombreusuario']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "¿Tiene el usuario un permiso específico?"
        # Respuesta más simple posible: sí, siempre
        return self.es_superusuario

    def has_module_perms(self, app_label):
        "¿Tiene el usuario permisos para ver la aplicación `app_label`?"
        # Respuesta más simple posible: sí, siempre
        return self.es_superusuario
    @property
    def is_staff(self):
        "¿El usuario es miembro del personal?"
        # La respuesta más simple posible: todos los administradores son personal
        return self.es_superusuario
