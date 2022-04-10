from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData,Contract,Transactions,RentHome
from django.http.response import HttpResponse
from django.http import HttpResponse

def userprofile(request):
    if(request.user.is_authenticated):
        user = request.user
        print(user.id)
        if(not user.is_superuser):
            userdata = UsersData.objects.get(user_id=user.id)
            if(userdata.usertype=="customer"):
                request.userdata = userdata
                print("You Are : ", user.first_name, user.last_name, userdata.usertype)
                return render(request,'user_profile.html')
            elif(userdata.usertype=="renter"):
                request.userdata = userdata
                homedata = RentHome.objects.all()
                context = {}
                context['homedata'] = homedata
                print(context['homedata'])
                context['userdata_id'] = userdata.id
                print("You Are : ", user.first_name, user.last_name, userdata.usertype)
                return render(request,'user_profile.html', context)
            else:
                return redirect('/')
        else:
            return redirect('/')

    else:
        return redirect('/')

def useredit(request):
    if(request.user.is_authenticated):
        user = request.user
        userdata = UsersData.objects.get(user_id=user.id)
        if(request.method=="GET"):
            editfname = request.GET.get("editfname")
            editlname = request.GET.get("editlname")
            editphone = request.GET.get("editphone")
            editaddress = request.GET.get("editaddress")
            editusername = request.GET.get("editusername")
            editemail = request.GET.get("editemail")
            editcity = request.GET.get("editcity")
            editstate = request.GET.get("editstate")

            if(editusername != user.username and User.objects.filter(username = editusername).exists()):
                return HttpResponse('Username already exists !!')
            if(editemail != user.email and User.objects.filter(email = editemail).exists()):
                return HttpResponse('Email already exists !!')
            if(editphone != userdata.mobile and UsersData.objects.filter(mobile = editphone).exists()):
                return HttpResponse('Mobile Number already exists !!')
            
            user.first_name = editfname
            user.last_name = editlname
            user.email = editemail
            user.username = editusername
            user.save()
            userdata.address = editaddress
            userdata.city = editcity
            userdata.state = editstate
            userdata.mobile = editphone
            userdata.save()
            
            return HttpResponse('fine')
        return redirect('/')
    return redirect('/')


def userdelete(request):
    if(request.user.is_authenticated):
        user = request.user
        userdata = UsersData.objects.get(user_id=user.id)
        if(request.method=="GET"):
            editusername = request.GET.get("editusername")
            auth_logout(request)
            user.delete()
            return HttpResponse('fine')
        else:
            return HttpResponse('Something went wrong !!')
    else:
        return redirect('/')
