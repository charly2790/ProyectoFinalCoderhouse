from django.contrib import admin

from Gestion_usuarios.models import Users,Persons,Posts,Bloggerhouse_levels

# Register your models here.
admin.site.register(Users)
admin.site.register(Persons)
admin.site.register(Posts)
admin.site.register(Bloggerhouse_levels)

