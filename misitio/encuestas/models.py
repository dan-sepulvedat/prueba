from django.db import models


class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('date published')

    def __str__(self):
        return self.descripcion


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion