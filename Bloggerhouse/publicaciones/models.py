from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class categoria(models.Model):
    name = models.CharField(max_length=40,blank=False,null=False)
    description = models.TextField(null = False)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class publicacion(models.Model):
    #1 usuario puede tener N publicaciones, pero una publicación solo puede pertenecer a un usuario
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    title = models.CharField(max_length=40,blank=False,null=False)        
    content = models.TextField(null = False)
    category = models.ForeignKey(categoria,on_delete=models.RESTRICT)    
    dt_creation = models.DateTimeField(default = timezone.now)
    dt_update = models.DateTimeField(default = timezone.now)
    main_image = models.ImageField(upload_to = 'post_image',blank=True, null=True)
    is_active = models.BooleanField(default=True)





 
