# Generated by Django 5.1.4 on 2025-03-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0002_rename_municipio_id_ubicacion_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='ciudad',
            field=models.CharField(default='Desconocido', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='pais',
            field=models.CharField(default='Desconocido', max_length=80),
            preserve_default=False,
        ),
    ]
