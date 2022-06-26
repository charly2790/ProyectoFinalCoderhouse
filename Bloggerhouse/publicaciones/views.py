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
    
#         product = Products.objects.get(id=pk)
#         context = {'product':product}
#         return render(request, 'product_detail.html', context=context)
#     except:
#         context = {'error':'El Producto no existe'}
#         return render(request, 'products.html', context=context)
@login_required
def create_publicacion(request):

    if request.method == 'POST':        
        form = Publicacion_form(request.POST)

        if form.is_valid():
            new_publicacion = publicacion.objects.create(
                user = request.user,
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                category = form.cleaned_data['category']            
            )
            context = {'new_publicacion': new_publicacion}
        else:
            context = {'error':form.errors}            
        
        return render(request, 'publicaciones/create_publicacion_template.html', context = context)
    else:
        print(f'usuario logueado: {request.user}')        
        form = Publicacion_form()
        context = {'form':form}
        return render(request,'publicaciones/create_publicacion_template.html',context = context)



