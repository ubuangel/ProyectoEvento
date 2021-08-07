# Generated by Django 3.2.5 on 2021-08-06 19:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='ec',
            field=models.ManyToManyField(through='equipo.Equipo_Ec', to=settings.AUTH_USER_MODEL),
        ),
    ]
