from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData,Contract,Transactions,RentHome

def addHome(request):
    if request.method == 'POST':
        if(request.user.is_authenticated):
            user = request.user
            userdata = UsersData.objects.get(user_id=user.id)
            if "renter" == userdata.usertype:
                address = request.POST.get('address')
                image1 = request.FILES.get('image1')
                image2 = request.FILES.get('image2')
                image3 = request.FILES.get('image3')
                image4 = request.FILES.get('image4')
                city = request.POST.get('city')
                state = request.POST.get('state')
                country = request.POST.get('country')
                rent = request.POST.get('rent')
                location = request.POST.get('location')
                temp_available = request.POST.get('is_available')
                is_available = True
                if "not_available"==temp_available:
                    is_available = False

                myhome = RentHome(uid=userdata.uid,address=address,image1=image1,image2=image2,image3=image3,image4=image4,city=city,state=state,country=country,rent=rent,location=location,is_available=is_available)
                myhome.save()
                redirect("/userprofile")
            else:
                redirect("/userprofile")
            
    return redirect("/")