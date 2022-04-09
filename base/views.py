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

def register_user(request):
    if(request.user.is_authenticated):
        return redirect('/')

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        img = request.FILES.get('img')

        if(User.objects.filter(username = username).exists()):
            messages.warning(request,"username is not available")
            return render(request,'register.html')
        elif(User.objects.filter(email = email).exists()):
            messages.warning(request,"Email is already taken")
            return render(request,'register.html')
        elif(UsersData.objects.filter(mobile = mobile).exists()):
            messages.warning(request,"Your Phone is already there")
            return render(request,'register.html')
        elif(usertype == "notnull" or usertype is None):
            messages.info(request,"Please Select usertype")
            return render(request,'register.html')

        user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
        user.save()
        user1 = UsersData(user=user,usertype=usertype,mobile=mobile,address=address,city=city,state=state,country=country,image=img)
        user1.save()
        auth_login(request,user)
        # messages.info(request,"Logged in successfully")
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
