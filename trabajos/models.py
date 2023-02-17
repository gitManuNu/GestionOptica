from django.db import models
from django.urls import reverse
from base.models import Persona, Doctor, LenteTratamiento, Armazon, ObraSocial

class Trabajo(models.Model):
    # Datos propios del trabajo
    detalle = models.CharField(max_length=250, verbose_name='detalle_trabajo')
    fecha = models.DateField(verbose_name='fecha_trabajo')
    tarea = models.CharField(max_length=250,verbose_name='tarea_trabajo',help_text='Tarea o actividad extra realizada sobre el trabajo')
    observacion = models.CharField(max_length=1000,verbose_name='observacion_trabajo')
    # Relaciones de tablas
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, verbose_name='persona', related_name='persona_trabajo')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='doctor',related_name='doctor_trabajo')
    fecha_receta = models.DateField(verbose_name='fecha_receta_trabajo',null=True)
    lente_con_tratamiento = models.ForeignKey(LenteTratamiento, on_delete=models.SET_NULL, null=True, verbose_name='lente_con_tratamiento',related_name='lente_con_tratamiento_trabajo')
    armazon = models.ForeignKey(Armazon,on_delete=models.SET_NULL,null=True,verbose_name='armazon',related_name='armazon_trabajo')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, verbose_name='obra_social',related_name='obra_social_trabajo')
    # Detalle del lente en si
    od_lejos_esf = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_derecho_lejos_esferico')
    od_lejos_cil = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_derecho_lejos_cilindrico')
    od_lejos_eje = models.IntegerField(null=True,verbose_name='ojo_derecho_lejos_eje')
    od_ad = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_derecho_adicion')
    od_cerca_esf = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_derecho_cerca_esferico')
    od_cerca_cil = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_derecho_cerca_cilindrico')
    od_cerca_eje = models.IntegerField(null=True,verbose_name='ojo_derecho_cerca_eje')

    oi_lejos_esf = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_izquierdo_lejos_esferico')
    oi_lejos_cil = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_izquierdo_lejos_cilindrico')
    oi_lejos_eje = models.IntegerField(null=True,verbose_name='ojo_izquierdo_lejos_eje')
    oi_ad = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_izquierdo_adicion')
    oi_cerca_esf = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_izquierdo_cerca_esferico')
    oi_cerca_cil = models.DecimalField(max_digits=4,decimal_places=2,null=True,verbose_name='ojo_izquierdo_cerca_cilindrico')
    oi_cerca_eje = models.IntegerField(null=True,verbose_name='ojo_izquierdo_cerca_eje')

    def get_absolute_url(self):
        return reverse('trabajo-detail-view', kwargs={'pk': self.pk})

    def __str__(self):
        return "TRABAJO DE %s, %s - %s - FECHA: %d" % (
            self.persona.apellido,
            self.persona.nombre,
            self.detalle,
            self.fecha
        )

    class Meta:
        verbose_name='Trabajo'
        verbose_name_plural='Trabajos'
