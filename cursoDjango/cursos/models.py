from tabnanny import verbose
from django.forms import IntegerField
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Cursos(models.Model):
    i = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.TextField(max_length=20,verbose_name="Nombre completo")
    curso = models.TextField(max_length=20,verbose_name="Nombre del curso")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    email = models.EmailField(max_length=200,verbose_name="Correo Electrónico")
    tiempo = models.BooleanField(
        default=False,verbose_name="Deseas obtener el curso intensivo")
    fecha = models.DateField(
        default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)#Fecha y tiempo
    update = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    
    def __str__(self):
        return self.curso

class Actividad(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Curso")
    desc = RichTextField(verbose_name="Descripción de la actividad")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Descripciones"
        verbose_name_plural = "Descripción"
        ordering = ["-created"]

        def __Str__(self):
            return self.desc