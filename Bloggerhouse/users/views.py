from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
#AuthenticationForm -> Formulario para autenticación
#UserCreationForm -> Formulario para creación de usuario
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from users.forms import custom_user_creation_form,profile_form,profile_main_fields_form
from users.models import Profile 

def detail_profile(request,pk):

    try:
        user_profile = Profile.objects.get(id = request.user.id)    
    except:
        user_profile = None
    
    if user_profile is not None:
        #El profile existe        
        if request.method == 'POST':
            form_profile = profile_form(request.POST,instance = user_profile)
            form_main_fields = profile_main_fields_form(request.POST,instance=request.user)

            if form_profile.is_valid() and form_main_fields.is_valid():                
                form_main_fields.save()
                new_profile = Profile.objects.create(
                    user = request.user,
                    birthday = form_profile.cleaned_data['birthday'],
                    country = form_profile.cleaned_data['country'],
                    img_profile = form_profile.cleaned_data['img_profile']
                )
                
                context = {'form_profile':form_profile,'form_main_fields':form_main_fields}
            else:
                context = {'form_profile_errors':form_profile.errors,'form_main_fields':form_main_fields.errors}                                
        else:
            form_profile = profile_form(instance = user_profile)
            form_main_fields = profile_main_fields_form(instance=request.user)
            
            context = {'form_profile':form_profile,'form_main_fields':form_main_fields}

        return render(request,'user_profile/user_profile_template.html',context = context)
    else:
        if request.method == 'POST':
            print('por 1)')
            form_profile = profile_form(request.POST,instance = user_profile)
            form_main_fields = profile_main_fields_form(request.POST,instance=request.user)

            if form_profile.is_valid() and form_main_fields.is_valid():
                print('por 1b')
              
                form_main_fields.save()
                print('por 1c')
                new_profile = Profile.objects.create(
                    user = request.user,
                    birthday = form_profile.cleaned_data['birthday'],
                    country = form_profile.cleaned_data['country'],
                    img_profile = form_profile.cleaned_data['img_profile']
                )
                
                context = {'form_profile':form_profile,'form_main_fields':form_main_fields}
            else:
                context = {'form_profile_errors':form_profile.errors,'form_main_fields':form_main_fields.errors}                
        else:
            print('por  2)')
            form_profile = profile_form()
            form_main_fields = profile_main_fields_form(instance=request.user)

            context = {'form_profile':form_profile,'form_main_fields':form_main_fields}
                
        return render(request,'user_profile/user_profile_template.html',context = context)

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
