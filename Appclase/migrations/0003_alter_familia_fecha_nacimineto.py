# Generated by Django 4.1.3 on 2022-12-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appclase', '0002_familia_fecha_nacimineto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fecha_nacimineto',
            field=models.DateField(blank=True),
        ),
    ]
