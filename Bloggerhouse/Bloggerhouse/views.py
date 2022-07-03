from django.shortcuts import render
from publicaciones.models import publicacion
from django.utils import timezone

def index(request):
    print(request.user)    
    publicaciones = publicacion.objects.all().order_by('-dt_update')
    context = {'publicaciones':publicaciones}    
    return render(request,'index.html',context = context)

#def create_user_view(request):

    
