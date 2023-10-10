from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacioon= models.DateField()


    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    estado = models.BooleanField(default=False)
    idusuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    idproyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=55)
    correo_electronico = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

