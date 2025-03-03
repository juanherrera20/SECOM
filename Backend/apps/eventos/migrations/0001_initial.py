# Generated by Django 5.1.4 on 2025-03-02 18:01

import apps.eventos.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('organizador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evento', to=settings.AUTH_USER_MODEL)),
                ('ubicacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='ubicacion.ubicacion')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_imagen', models.ImageField(max_length=250, upload_to=apps.eventos.models.get_image_upload_path)),
                ('orden', models.IntegerField(default=1)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='eventos.evento')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
                'ordering': ['orden'],
            },
        ),
    ]
