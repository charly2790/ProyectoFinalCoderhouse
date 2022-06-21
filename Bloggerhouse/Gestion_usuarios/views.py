from multiprocessing import context
from django.shortcuts import render,redirect
from Gestion_usuarios.models import Persons
from Gestion_usuarios.models import Users
from Gestion_usuarios.models import Posts
from Gestion_usuarios.forms import Users_form
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
#AuthenticationForm -> Formulario para autenticación
#UserCreationForm -> Formulario para creación de usuario
from django.contrib.auth import authenticate,login,logout 





def post_detail_view(request,pk,user_loged):

    print(f"pk: {pk}, user_loged: {user_loged}'")
    try:
        post = Posts.objects.get(id=pk)
        context = {'post':post,'user_loged':user_loged}
        return render(request,'user_actions/create_post_template.html',context=context)        
    except:
        context = {'ERROR_02': 'ERROR_02','user_loged': user_loged}
        return render(request,'user_actions/create_post_template.html',context=context)

def post_delete_view(request,pk,user_loged):
    
    try:
        #Viene por GET cuando es llamado desde el botón 'borrar' de la vista 'show_user_posts_view'
        post = Posts.objects.get(id = pk)
        if request.method == 'GET':            
            context = {'post':post}
            
        else: 
            post.delete()
            context = {'message':'Post eliminado correctamente'}
        
        return render(request,'user_actions/delete_post_template.html',context=context)

    except:
        context = {'message':'¡Error! El post no existe'}
        
        return render(request,'user_actions/delete_post_template.html',context=context)




def show_user_posts_view(request):

    print(request.POST['email_user_logged'])
    posts = Posts.objects.filter(email_autor__contains = request.POST['email_user_logged'])
    
    print(f"Tipo de datos: {type(posts)}, cantidad de registros: {len(posts)}" )
    
    if len(posts) > 0:
        context = {'posts': posts}
    else:
        context = {'ERROR_01': 'ERROR_01'}
    
    return render(request,'user_actions/show_user_posts_template.html',context = context)    

def create_post_process(request):
    if request.method == 'POST':
        
        new_post = Posts.objects.create(
        email_autor = request.POST['email'],
        topic = request.POST['topic'],
        content = request.POST['content'],       
        )
        context = {'new_post' : new_post}
        
        return render(request,'user_actions/post_view_template.html',context = context)

def create_post_view(request):
    try:
        email_user = request.POST['email']
    except:
        email_user = None
    
    if email_user != None:
        context = {'user_loged': email_user}
    else:
        context = {}
    
    return render(request,'user_actions/create_post_template.html',context = context)


def user_login_view(request):
    
    try:
        login_error = request.POST['login_error']
    except:
        login_error = None

    if login_error != None:
        context = {'login_error':login_error}
    else:
        context = {}
    
    return render(request,'user_login_template.html',context = context)

def user_login_process(request):    

    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
                
        try:
            user_loged = Users.objects.get(email = em)            
            if user_loged.password == passw:                
                context = {'user_loged': user_loged}                                           
                return render(request,'user_actions/user_main_screen_template.html', context = context)
            else:                
                context = {'login_error': 'Contraseña incorrecta'}
                return render(request,'user_login_template.html',context = context)

        except:            
            context = {'login_error': 'No existe un usuario asociado al correo electrónico ingresado'}
            return render(request,'user_login_template.html',context = context)



# Create your views here.
def create_user_view(request):
    print(request.method)
    if request.method == 'GET':
        form = Users_form()
        context = {'form': form}
        return render(request,'create_user_template.html', context = context)
    else:
        form = Users_form(request.POST)
        if form.is_valid():
            new_user = Users.objects.create(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                alias = form.cleaned_data['alias']
            )
            context = {'new_user': new_user}
        return render(request,'create_user_template.html',context = context)


def search_user_view(request):
    users = Users.objects.filter(email__contains = request.GET['search'])
    context = {'users': users}
    return render(request,'search_user_template.html',context = context)

def person_data_view(request):
    user_email = request.GET['email']
    context = {'user_email': user_email}
    return render(request,'person_data_template.html', context = context)

def create_person_view(request):
    if request.method == 'POST':
        
        new_person = Persons.objects.create(
        email = request.POST['email'],
        name = request.POST['name'],
        surname = request.POST['surname'],
        id_number = request.POST['id_number'],
        birthday = request.POST['birthday'],
        country = request.POST['country'],
        state = request.POST['state'],
        city = request.POST['city'],
        street = request.POST['street'],
        number = request.POST['number']
        )
        context = {'new_person' : new_person}
        
        return render(request,'person_data_template.html',context = context)
    
    else:
        context = {'message':'Error - No vino por POST'}
        return render(request,'person_data_template.html',context = context)
    

