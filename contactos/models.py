from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre