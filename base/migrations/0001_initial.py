# Generated by Django 4.1.2 on 2022-12-23 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='obra_social')),
            ],
            options={
                'verbose_name': 'Obra Social',
                'verbose_name_plural': 'Obras Sociales',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=60, verbose_name='apellido')),
                ('nombre', models.CharField(max_length=60, verbose_name='nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='dirección')),
                ('mail', models.EmailField(max_length=255, verbose_name='mail')),
                ('tel1', models.CharField(max_length=25, verbose_name='telefono_1')),
                ('tel2', models.CharField(max_length=25, verbose_name='telefono_2')),
                ('obra_social', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.obrasocial', verbose_name='persona_ob_soc')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
