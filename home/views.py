from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginpage(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #check credential
        user = authenticate( username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
               return render(request, 'login.html')

        # No backend authenticated the credentials
        
    
    return render(request, 'login.html')
       

def logoutuser(request):
    logout(request)
    return redirect("/login")

def register(request):
    form=UserCreationForm()

    return render (request, "register.html")