# Generated by Django 4.2 on 2023-05-08 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primera_aplicacion', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datosproveedor',
            options={'permissions': (('permiso_edicion', 'permiso para editar card'),)},
        ),
    ]
