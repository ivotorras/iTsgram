from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    user = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=255, blank=True)
    docfile = models.FileField(upload_to='documents/')
    fecha = models.CharField(max_length=255, blank=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True)

    
    def publicado(self):
            self.fecha = timezone.now()
            self.save()

    def __str__(self):
        return self.user

    
class Comentarios(models.Model):
    f_comentada = models.ForeignKey(Document, on_delete=models.CASCADE)
    user =  models.CharField(max_length=32, blank=False)
    comentario = models.CharField(max_length=255, blank=False)
    
class Likes(models.Model):
    f_comentada = models.ForeignKey(Document, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def aumentar(self):
        self.cantidad += 1
        self.save()    


    
    
    
class Publisher(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
		return self.name

    def __str__(self):
        return self.name
        