"""Bloggerhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Bloggerhouse.views import index
from Gestion_usuarios.views import create_user_view,search_user_view,person_data_view,create_person_view,user_login_view,user_login_process,create_post_view,create_post_process

urlpatterns = [    
    path('',index,name='index'),
    path('create-user/',create_user_view,name = 'create-user-view'),
    path('search-user/',search_user_view,name = 'search-user-view'),
    path('person-data/',person_data_view,name = 'person-data-view'),
    path('create-person-view/',create_person_view,name = 'create-person-view'),
    path('user-login/',user_login_view,name = 'user-login-view'),
    path('user-login-process/',user_login_process,name = 'user-login-process'),
    path('create-post/',create_post_view,name = 'create_post_view'),
    path('create-post-process/',create_post_process,name = 'create_post_process'),
    path('Gestion_usuarios/',include('Gestion_usuarios.urls')),

    
]
