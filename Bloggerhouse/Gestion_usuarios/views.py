from django.shortcuts import render
from Gestion_usuarios.models import Users
from Gestion_usuarios.forms import Users_form

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

#def search_product_view(request):
#    print(request.GET)
#    product = Products.objects.get()
#    products = Products.objects.filter(name__contains = request.GET['search'])
#    context = {'products':products}
#    return render(request, 'search_product.html', context = context)
        

