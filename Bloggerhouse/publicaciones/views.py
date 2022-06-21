from django.shortcuts import render
from publicaciones.forms import Publicacion_form

# Create your views here.

def create_publicacion(request):

    if request.method == 'POST':
        pass
    else:
        form = Publicacion_form()
        context = {'form':form}
        return render(request,'publicaciones/create_publicacion_template.html',context = context)



