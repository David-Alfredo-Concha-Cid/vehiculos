# Generated by Django 4.2.2 on 2023-07-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Visualizar catalogos')]},
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[['Particular', 'Particular'], ['transporte', 'transporte'], ['carga', 'carga']], default='Particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[['@fiat', 'Fiat'], ['@chevrolet', 'Chevrolet'], ['@ford', 'Ford'], ['@toyota', 'Toyota']], default='@ford', max_length=20),
        ),
    ]
