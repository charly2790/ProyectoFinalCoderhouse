from datetime import datetime
from django.db import models
from django.forms import DateField

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=40, blank = False, null = False)
    password = models.CharField(max_length=40, blank=False,null = False)
    alias = models.CharField(max_length=40)
    rol = models.CharField(max_length=40,default = 'BLOGGER_BASIC')
    fail_connection_attemps = models.IntegerField(default = 0)
    blocked = models.BooleanField(default = True)
    #En lugar de datetime.now() django sugiere utilizar django.utils.timezone.now
    dt_last_connection = models.DateTimeField(default = datetime.now())
    dt_creation = models.DateTimeField(default = datetime.now())
    bloggerhouse_level = models.CharField(max_length=40,default = 'BLOGGER_NEWBIE')

class Persons(models.Model):
    email = models.EmailField(max_length=40, blank = False, null = False)        
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    id_number = models.CharField(max_length=40)
    birthday = models.DateField(default = datetime.now())    
    country = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    number = models.IntegerField()

class Bloggerhouse_levels(models.Model):
    id_level = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    
class Posts(models.Model):
    email_autor = models.EmailField(max_length=40,blank = False, null = False)
    topic = models.CharField(max_length = 40,blank=False,null=False)
    content = models.TextField(null = False)
    likes = models.IntegerField(default = 0)
    dt_creation = models.DateTimeField(default = datetime.now())
