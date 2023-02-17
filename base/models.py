from django.db import models
from django.urls import reverse

class ObraSocial(models.Model):
    descripcion = models.CharField(max_length=60,verbose_name='obra_social',null=False,blank=False)
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name='Obra Social'
        verbose_name_plural='Obras Sociales'


class Persona(models.Model):
    apellido = models.CharField(max_length=60,verbose_name='apellido',null=False,blank=False)
    nombre = models.CharField(max_length=60,verbose_name='nombre',null=False,blank=False)
    direccion = models.CharField(max_length=100,verbose_name='dirección',null=True,blank=True)
    mail = models.EmailField(max_length=255,verbose_name='mail',null=True,blank=True)
    tel1 = models.CharField(max_length=25,verbose_name='telefono_1',null=True,blank=True)
    tel2 = models.CharField(max_length=25,verbose_name='telefono_2',null=True,blank=True)
    obra_social = models.ForeignKey(ObraSocial,null=True,verbose_name='persona_ob_soc',on_delete=models.SET_NULL,related_name='persona_ObraSocial')
    
    def get_absolute_url(self):
        return reverse('persona-detail-view', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s, %s" % (self.apellido,self.nombre)

    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'
        ordering=['apellido','nombre']


class Doctor(models.Model):
    apellido = models.CharField(max_length=60,verbose_name='apellido',null=False,blank=False)
    nombre = models.CharField(max_length=60,verbose_name='nombre',null=False,blank=False)
    ciudad = models.CharField(max_length=60,verbose_name='ciudad',null=False,blank=False)

    def get_absolute_url(self):
        return reverse('doctor-detail-view', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.apellido

    class Meta:
        verbose_name='Doctor'
        verbose_name_plural='Doctores'


class Lente(models.Model):
    descripcion = models.CharField(max_length=60, verbose_name='desc_lente',null=False,blank=False)

    class Meta:
        verbose_name='Lente'
        verbose_name_plural='Lentes'


class Tratamiento(models.Model):
    descripcion = models.CharField(max_length=60, verbose_name='desc_tratamiento',null=False,blank=False)

    class Meta:
        verbose_name='Tratamiento'
        verbose_name_plural='Tratamientos'


class LenteTratamiento(models.Model):
    descripcion = models.CharField(max_length=60, verbose_name='lente_con_tratamiento',null=False,blank=False)
    lente = models.ForeignKey(Lente,null=False,verbose_name='lente',on_delete=models.CASCADE,related_name='lente_lenteTramamiento')
    tratamiento = models.ForeignKey(Lente,null=True,verbose_name='tratamiento',on_delete=models.SET_NULL,related_name='tratamiento_lenteTramamiento')
    
    def __str__(self):
        return self.descripcion
    

    class Meta:
        verbose_name='Lente con Tratamiento'
        verbose_name_plural='Lentes con Tratamiento'


class Proveedor(models.Model):
    descripcion = models.CharField(max_length=60, verbose_name='desc_proveedor',null=False,blank=False)
    # categoria

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'


class Armazon(models.Model):
    descripcion = models.CharField(max_length=60, verbose_name='desc_armazon',null=False,blank=False)
    proveedor = models.CharField(max_length=60, verbose_name='proveedor_armazon',null=True,blank=True)
    
    def __str__(self):
        return self.descripcion
    

    class Meta:
        verbose_name='Armazon'
        verbose_name_plural='Armazones'
