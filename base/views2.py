from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData,Contract,Transactions,RentHome

def userprofile(request):
    if(request.user.is_authenticated):
        user = request.user
        userdata = UsersData.objects.get(user_id=user.id)
        if(userdata.usertype=="customer"):
            print("You Are : ", user.first_name, user.last_name)
            return render(request,'user_profile.html')
        elif(userdata.usertype=="renter"):
            request.userdata = userdata
            print("You Are : ", user.first_name, user.last_name)
            return render(request,'user_profile.html')
        else:
            return redirect('/')

    else:
        return redirect('/')