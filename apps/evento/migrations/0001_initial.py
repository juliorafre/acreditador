# Generated by Django 2.1.1 on 2018-12-23 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcíon')),
                ('ubicacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ubicacíon')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha del evento')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Codigo Evento')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['-created'],
            },
        ),
    ]
