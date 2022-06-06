from django.shortcuts import render

def index(request):
    return render(request,'index.html',context = {})

#def create_user_view(request):

    
