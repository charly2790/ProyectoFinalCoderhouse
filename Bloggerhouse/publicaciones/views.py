from django.shortcuts import render,redirect,reverse
from publicaciones.models import publicacion
from publicaciones.forms import Publicacion_form
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def search_publicacion_view(request):
    publicaciones = publicacion.objects.filter(title__icontains = request.GET['search'])
    
    if len(publicaciones) == 0:
        context = {'error_no_results':'No se encontraron posts con ese título.'}
        return redirect('index')
        #return render(request,'index.html',context = context)
    elif publicaciones == 1:
        context = {'publicacion': publicaciones.first()}
        return render(request,'publicaciones/detail_publicacion_template.html',context=context)
    else:
        context = {'publicaciones': publicaciones}
        return render(request,'publicaciones/list_publicacion_template.html',context = context)

@login_required
def delete_publicacion_view(request,pk):

    if request.method == 'POST':
        try:
            post = publicacion.objects.get(id=pk) 
        except:
            post = None
        
        if post != None:
            post.delete()
            context = {'success_message':'La publicación ha sido eliminada correctamente'}
        else:
            context = {'error':'¡Error! No se encontró la publicación'}
        
        return render(request,'publicaciones/delete_publicacion_template.html',context = context)
    else:
        try:
            post = publicacion.objects.get(id = pk)
            context = {'post': post}
        except:
            context = {'error':'¡Error! No se encontró la publicación.'}

        return render(request,'publicaciones/delete_publicacion_template.html',context = context)

def update_publicacion_view(request,pk):
    
    try:
        post = publicacion.objects.get(id=pk)   
    except:
        post = None

    if request.method == 'POST':
        
        if post != None:
            form = Publicacion_form(request.POST,request.FILES or None, instance = post)
            form.instance.dt_update = timezone.now()
                        
            if form.is_valid():
                form.save()
                form = Publicacion_form(instance = form.instance)
                context = {'form':form,'success_message':'La publicación se ha actualizado correctamente.'}
            else:
                context = {'error': form.errors}    
        else:
            context = {'error':'¡Error! No se encontró la publicación.'}
        
    else:
        if post != None:
            form = Publicacion_form(instance = post)
            context = {'form':form}
        else:
            context = {'error':'¡Error! No se encontró la publicación.'}
        
    return render(request,'publicaciones/update_publicacion_template.html',context = context)

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

        print('antes de validad el form')
        if form.is_valid():
            print('valida el form')
            #print(form.cleaned_data['main_image'])
            new_publicacion = publicacion.objects.create(
                user = request.user,
                title = form.cleaned_data['title'],
                main_image = form.cleaned_data['main_image'],
                content = form.cleaned_data['content'],
                category = form.cleaned_data['category']            
            )
            context = {'publicacion': new_publicacion,'message':'¡Publicación creada con exito!'}
            print('crea la pubicación')
            return render(request, 'publicaciones/detail_publicacion_template.html', context = context)
        else:
            print('Sale por el else')            
            form = Publicacion_form()
            context = {'form_errors':form.errors,'form':form}                        
            return render(request, 'publicaciones/create_publicacion_template.html', context = context)
    else:
        print(f'usuario logueado: {request.user}')        
        form = Publicacion_form()
        context = {'form':form}
        return render(request,'publicaciones/create_publicacion_template.html',context = context)



