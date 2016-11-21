from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Document(models.Model):
    #description = models.CharField(max_length=255, blank=True)
    docfile = models.FileField(upload_to='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

    
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
		return self.name

    def __str__(self):
        return self.name
        