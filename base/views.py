from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData,Contract,Transactions,RentHome


# Create your views here.


def index(request):
    return render(request, "index.html")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request,user)
            messages.info(request,"Logged in successfully")
            return redirect('login')
        messages.warning(request,"Username or Password incorrect")
    return render(request, 'login.html')


def register_user_page(request):
    return render(request,'register.html')


def register_user(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        img = request.FILES.get('img')

        if(User.objects.filter(username = username).exists()):
            messages.warning(request,"username is not available")
            return redirect('register')
        elif(User.objects.filter(email = email).exists()):
            messages.warning(request,"Email is already taken")
            return redirect('register')
        elif(UsersData.objects.filter(phone = phone).exists()):
            messages.warning(request,"Your Phone is already there")
            return redirect('register')
        # messages.info(request,"Email is already taken")



        print(fname)
    return render(request,'register.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
