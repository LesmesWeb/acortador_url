from django.db import models
from django.urls import reverse
from hashids import Hashids
import datetime

# Create your models here.
class EnlaceQuerySet(models.QuerySet):
    def decode_enlace(self, codigo):
        decode = Hashids(min_lenght=4,alphabet='abcdefghijklmnopqrstuvwxyz').decode(codigo)[0]
        self.filter(pk=decode).update(contador=models.F('contador') + 1)
        return self.filter(pk=decode).first().url

    def total_enlaces(self):
        return self.count()
    
    def total_redirecciones(self):
        return self.aggregate(redirecciones=models.Sum('contador'))

    def fechas(self,pk):
        #values: convierte el query en forma de diccionario
        return self.values('fecha').annote(
            julio=models.Sum('contador',filter=models.Q(filter__gte=datetime.date(2019,7,1),
            filter__lte=datetime.date(2019,7,31)))
        ).filter(pk=pk)

class Enlace(models.Model):
    url = models.URLField()
    codigo = models.CharField(max_length=8,blank=True)
    fecha = models.DateField(auto_now_add=True)         #se registra la fecha una sola vez
    contador = models.PositiveIntegerField(default=0)   #solo almacenara numero positivos

    #sobre escribiremos el metodo class meta el cual contiene propiedades interesantes
    class Meta:
        verbose_name = 'Enlace URL'
        verbose_name_plural = "Enlaces URLS"

    #este metodo devuelve de una forma mas legible de una intancia de un enlace porque sin él traeria un object en vez del nombre del campo
    def __str__(self):
        return f"URL: {self.url} Codigo: {self.codigo}"

    #cada ves que se le llama podemos activar una acción para que se incluya en el guardado
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if not self.codigo:
            self.codigo = Hashids(min_lenght=4,alphabet='abcdefghijklmnopqrstuvwxyz').encode(self.pk)
            self.save()
    
    #como crear una url con base en un objeto
    def get_absolute_url(self):
        return reverse('core:detalle', kwargs={'pk': self.pk})