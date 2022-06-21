from django.contrib import admin
from django.urls import path,include
from Bloggerhouse.views import index
from publicaciones.views import create_publicacion

urlpatterns = [    
path('create-post/',create_publicacion, name = 'create_publicacion'),
] 