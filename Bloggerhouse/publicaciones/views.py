from django.shortcuts import render
from publicaciones.models import publicacion
from publicaciones.forms import Publicacion_form
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def detail_publicaciones(request,pk):
    try:        
        post = publicacion.objects.get(id=pk)         
        context = {'publicacion': post}
        
    except:
        context = {'error': '¡Publicación inexistente!'}        

    return render(request,'publicaciones/detail_publicacion_template.html',context=context)
            

@login_required
def create_publicacion(request):

    if request.method == 'POST':        
        form = Publicacion_form(request.POST, request.FILES or None)

        if form.is_valid():
            print(form.cleaned_data['main_image'])
            new_publicacion = publicacion.objects.create(
                user = request.user,
                title = form.cleaned_data['title'],
                main_image = form.cleaned_data['main_image'],
                content = form.cleaned_data['content'],
                category = form.cleaned_data['category']            
            )
            context = {'publicacion': new_publicacion,'message':'¡Publicación creada con exito!'}
            return render(request, 'publicaciones/detail_publicacion_template.html', context = context)
        else:            
            form = Publicacion_form()
            context = {'form_errors':form.errors,'form':form}                        
            return render(request, 'publicaciones/create_publicacion_template.html', context = context)
    else:
        print(f'usuario logueado: {request.user}')        
        form = Publicacion_form()
        context = {'form':form}
        return render(request,'publicaciones/create_publicacion_template.html',context = context)



