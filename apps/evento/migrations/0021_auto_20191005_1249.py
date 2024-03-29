# Generated by Django 2.1.1 on 2019-10-05 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0020_auto_20190419_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_config', models.CharField(blank=True, editable=False, max_length=255, verbose_name='ID')),
                ('ver_disp', models.BooleanField(default=False, verbose_name='Verificador de Disponibilidad')),
                ('ver_limit', models.BooleanField(default=False, verbose_name='Verificador de Limite')),
                ('num_limit', models.IntegerField(default=0, verbose_name='Numero de asistentes')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Configuracion de Evento',
                'verbose_name_plural': 'Configuraciones de Eventos',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='evento',
            name='area',
            field=models.CharField(blank=True, choices=[('Vinculación con el Medio y Extensión', 'Vinculación con el Medio y Extensión'), ('Dirección de Desarrollo Académico', 'Dirección de Desarrollo Académico'), ('Dirección Educación Continua y Online', 'Dirección Educación Continua y Online'), ('Dirección de Docencia', 'Dirección de Docencia'), ('Dirección de Innovación e Investigación Aplicada', 'Dirección de Innovación e Investigación Aplicada'), ('Dirección de Formación General', 'Dirección de Formación General'), ('Dirección de Formación Cristiana y Ética', 'Dirección de Formación Cristiana y Ética'), ('Dirección de Procesos y Tecnologías', 'Dirección de Procesos y Tecnologías'), ('Dirección de Personas', 'Dirección de Personas'), ('Dirección de Gestión y Planificación', 'Dirección de Gestión y Planificación'), ('Dirección de Administración y Finanzas', 'Dirección de Administración y Finanzas'), ('Dirección de Operación y Desarrollo', 'Dirección de Operación y Desarrollo'), ('Dirección de Infraestructura', 'Dirección de Infraestructura'), ('Proyectos y Servicios Duoc UC', 'Proyectos y Servicios Duoc UC'), ('Dirección de Educación Continua y Servicios', 'Dirección de Educación Continua y Servicios'), ('Dirección de Calidad Académica', 'Dirección de Calidad Académica'), ('Dirección de Pastoral', 'Dirección de Procesos de Acreditación'), ('Dirección de Comunicación y Marketing', 'Dirección de Comunicación y Marketing'), ('Dirección de Empleabilidad y Vinculación con el Medio', 'Dirección de Empleabilidad y Vinculación con el Medio'), ('Dirección de Relaciones Internacionales', 'Dirección de Relaciones Internacionales'), ('Dirección de Desarrollo Estudiantil', 'Dirección de Desarrollo Estudiantil'), ('Dirección de Pastoral', 'Dirección de Pastoral'), ('Dirección de Contraloría', 'Dirección de Contraloría'), ('No especificado', 'No especificado')], default='No especificado', max_length=255, null=True, verbose_name='Área organizadora'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='sede',
            field=models.CharField(blank=True, choices=[('Casa Central', 'Casa Central'), ('Antonio Varas', 'Antonio Varas'), ('Alameda', 'Alameda'), ('Campus Arauco', 'Campus Arauco'), ('Maipú', 'Maipú'), ('Melipilla', 'Melipilla'), ('Padre Alonso Ovalle', 'Padre Alonso Ovalle'), ('Plaza Norte', 'Plaza Norte'), ('Plaza Oeste', 'Plaza Oeste'), ('Plaza Vespucio', 'Plaza Vespucio'), ('Puente Alto', 'Puente Alto'), ('San Andrés de Concepción', 'San Andrés de Concepción'), ('San Bernardo', 'San Bernardo'), ('San Carlos de Apoquindo', 'San Carlos de Apoquindo'), ('San Joaquín', 'San Joaquín'), ('Valparaíso', 'Valparaíso'), ('Viña del Mar', 'Viña del Mar'), ('No especificado', 'No especificado')], default='No especificado', max_length=255, null=True, verbose_name='Sede organizadora'),
        ),
        migrations.AddField(
            model_name='evento',
            name='config',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='evento.ConfigEvento', verbose_name='Configuracion'),
        ),
    ]
