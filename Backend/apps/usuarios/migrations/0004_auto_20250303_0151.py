from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20250303_0150'),  # Asegúrate de que sea la última migración válida
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img_profile',
            field=models.ImageField(upload_to='ImagenesPerfil', null=True, blank=True),
        ),
    ]