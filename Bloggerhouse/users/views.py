from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
#AuthenticationForm -> Formulario para autenticación
#UserCreationForm -> Formulario para creación de usuario
from django.contrib.auth import authenticate,login,logout
from users.forms import custom_user_creation_form 

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = custom_user_creation_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            context = {'message':f'¡Gracias por registrarse en Bloggerhouse!¡Bienvenido {username}!'}            
            return render(request, 'index.html',context = context)
        else:            
            errors = form.errors
            form = custom_user_creation_form()
            context = {'errors':errors,'form':form}            
            return render (request, 'auth/user_register_template.html', context = context)

    else:
        form = custom_user_creation_form()
        context = {'form' : form}
        return render(request,'auth/user_register_template.html',context = context)
    
    

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        print('llega al is valid')
        if form.is_valid():
            print('pasa el is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']            
            # 1) Si las credenciales son validas retorna el objeto usuario, caso contrario None
            user = authenticate(username = username,password = password)
            print('despues del authenticate')
            if user is not None:
                print('login not none')                
                login(request,user)
                context = {'message':f'¡Bienvenido {username}!'}
                return render(request, 'index.html',context = context)
            else:
                print('login none')                       
                context = {'errors': 'Usuario y/o contraseña invalidos'}
                form = AuthenticationForm()                
                return render(request,'auth/user_login_template.html',context = context)
        else:
            print('no pasa el is valid')        
            #Guardamos los errores en una variable
            errors = form.errors        
            #creamos nuevamente el formulario
            form = AuthenticationForm()        
            context = {'errors':errors,'form':form}
            return render(request,'auth/user_login_template.html',context = context)
    else:

        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'auth/user_login_template.html',context = context)

def logout_view(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect('index')