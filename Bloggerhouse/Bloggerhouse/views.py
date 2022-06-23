from django.shortcuts import render
from publicaciones.models import publicacion

def index(request):
    print(request.user)    
    publicaciones = publicacion.objects.all()
    print(publicaciones)
    context = {'publicaciones':publicaciones}    
    return render(request,'index.html',context = context)

#def create_user_view(request):

    
