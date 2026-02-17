from django.db import models

class usuarios(models.Model):
    NombreUsuario = models.TextField(max_length=255)
    Correo = models.TextField(max_length=255)
    Password = models.TextField(max_length=255) 

    def __str__(self):
        return str(self.NombreUsuario)




class score(models.Model):
    Puntos = models.IntegerField()
    Usuario = models.TextField(max_length=255)


