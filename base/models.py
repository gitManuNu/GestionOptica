from django.db import models

# Create your models here.

class ObraSocial(models.Model):
    descripcion = models.CharField(max_length=60,verbose_name='obra_social')
    class Meta:
        verbose_name='Obra Social'
        verbose_name_plural='Obras Sociales'

class Persona(models.Model):
    apellido = models.CharField(max_length=60,verbose_name='apellido')
    nombre = models.CharField(max_length=60,verbose_name='nombre')
    direccion = models.CharField(max_length=100,verbose_name='dirección')
    mail = models.EmailField(max_length=255,verbose_name='mail')
    tel1 = models.CharField(max_length=25,verbose_name='telefono_1')
    tel2 = models.CharField(max_length=25,verbose_name='telefono_2')
    obra_social = models.ForeignKey(ObraSocial,null=True,verbose_name='persona_ob_soc',on_delete=models.SET_NULL)
    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'
        ordering=['apellido','nombre']