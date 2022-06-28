from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=64)
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)                            
    birthday = models.DateField(default = timezone.now)    
    country = models.OneToOneField(Country,on_delete=models.RESTRICT)
    img_profile = models.ImageField(upload_to = 'profile_images',blank=True, null=True)


   
