from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login 
from django.contrib.auth.models import User
from django.contrib import messages


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
