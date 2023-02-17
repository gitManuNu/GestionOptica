# Generated by Django 4.1.2 on 2023-02-17 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20230113_2037'),
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persona_trabajo', to='base.persona', verbose_name='persona'),
        ),
    ]
