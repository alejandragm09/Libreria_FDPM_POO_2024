from django.db import models
from django.urls import reverse

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('libros:libro_detail', args=[str(self.id)])