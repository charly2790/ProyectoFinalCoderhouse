from django.contrib import admin
from publicaciones.models import publicacion,categoria
from users.models import Profile,Country

# Register your models here.
admin.site.register(publicacion)
admin.site.register(categoria)
admin.site.register(Profile)
admin.site.register(Country)