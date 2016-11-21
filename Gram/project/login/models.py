from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Document(models.Model):
    #description = models.CharField(max_length=255, blank=True)
    docfile = models.FileField(upload_to='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

    
    
    
class Publisher(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
		return self.name

    def __str__(self):
        return self.name
        