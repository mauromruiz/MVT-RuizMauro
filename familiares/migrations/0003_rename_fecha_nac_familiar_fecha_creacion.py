# Generated by Django 4.1.1 on 2022-10-05 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_familiar_fecha_nac'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='fecha_nac',
            new_name='fecha_creacion',
        ),
    ]