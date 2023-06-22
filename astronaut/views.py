

from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request, "astronaut/signin.html")

def index(request):
    return render(request, "astronaut/index.html")

def signup(request):

    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        user_name = request.POST['user_name']
        password = request.POST['password']

        if User.objects.filter(username=user_name):
            messages.error(request, "Username already exist! Please try other username")
            return redirect('signin')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signin')
        
        
        myuser = User.objects.create_user(user_name, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        # Welcome Email

       # subject = "Welcome to Cebu Tour Guide Web"
       # message = "Hello" + myuser.first_name 
       

       
       


    return render(request, "astronaut/signin.html")

  

def signin(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(username=user_name, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return HttpResponseRedirect('index', {'firstname': fname})

        else:
            messages.error(request, "Username or Password Invalid")
            return redirect('signin')

    return render(request, "astronaut/signin.html")

@login_required(login_url="signin")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")




    return HttpResponseRedirect('signin')

