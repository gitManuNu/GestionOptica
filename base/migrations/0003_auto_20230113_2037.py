# Generated by Django 3.2.6 on 2023-01-13 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armazon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='desc_armazon')),
                ('proveedor', models.CharField(blank=True, max_length=60, null=True, verbose_name='proveedor_armazon')),
            ],
            options={
                'verbose_name': 'Armazon',
                'verbose_name_plural': 'Armazones',
            },
        ),
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='desc_lente')),
            ],
            options={
                'verbose_name': 'Lente',
                'verbose_name_plural': 'Lentes',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='desc_proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='desc_tratamiento')),
            ],
            options={
                'verbose_name': 'Tratamiento',
                'verbose_name_plural': 'Tratamientos',
            },
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctores'},
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='dirección'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mail',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='mail'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='obra_social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persona_ObraSocial', to='base.obrasocial', verbose_name='persona_ob_soc'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tel1',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='telefono_1'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tel2',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='telefono_2'),
        ),
        migrations.CreateModel(
            name='LenteTratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='lente_con_tratamiento')),
                ('lente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lente_lenteTramamiento', to='base.lente', verbose_name='lente')),
                ('tratamiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tratamiento_lenteTramamiento', to='base.lente', verbose_name='tratamiento')),
            ],
            options={
                'verbose_name': 'Lente con Tratamiento',
                'verbose_name_plural': 'Lentes con Tratamiento',
            },
        ),
    ]