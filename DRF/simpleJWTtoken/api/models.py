from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    roll= models.IntegerField()
    city= models.CharField(max_length=100)
    
    
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
