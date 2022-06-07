from django.shortcuts import render
from Gestion_usuarios.models import Persons
from Gestion_usuarios.models import Users
from Gestion_usuarios.forms import Users_form


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
    print("entra")

    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
        print(f'em: {em} - passw: {passw}')
        
        try:
            user_loged = Users.objects.get(email = em)            
            if user_loged.password == passw:                
                context = {'user_loged': user_loged}                                           
                return render(request,'user_main_screen_template.html', context = context)
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





#def search_product_view(request):
#    print(request.GET)
#    product = Products.objects.get()
#    products = Products.objects.filter(name__contains = request.GET['search'])
#    context = {'products':products}
#    return render(request, 'search_product.html', context = context)
        

