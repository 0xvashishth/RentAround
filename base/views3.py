from contextlib import nullcontext
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData,Contract,Transactions,RentHome

def addhome(request):
    if request.method == 'POST':
        if(request.user.is_authenticated):
            user = request.user
            userdata = UsersData.objects.get(user_id=user.id)
            if "renter" == userdata.usertype:
                address = request.POST.get('aaddress')
                image1 = request.FILES.get('aimg1')
                image2 = request.FILES.get('aimg2')
                image3 = request.FILES.get('aimg3')
                image4 = request.FILES.get('aimg4')
                city = request.POST.get('acity')
                state = request.POST.get('astate')
                country = request.POST.get('acountry')
                pincode = request.POST.get('apincode')
                description = request.POST.get('adescription')
                rent = request.POST.get('aprice')
                # location = request.POST.get('location')
                is_available = request.POST.get('mode_rent')
                rent_capacity = request.POST.get('acapacity')
                is_available = True
                if "not_avail"==is_available:
                    is_available = False

                myhome = RentHome(uid=userdata,address=address,image1=image1,image2=image2,image3=image3,image4=image4,city=city,state=state,country=country,pincode=pincode,rent=rent,is_available=is_available,rent_capacity=rent_capacity,description=description)
                myhome.save()
                print("Home saved!!")
                return redirect("/userprofile")
            else:
                return redirect("/userprofile")
        return redirect("/")            
    return redirect("/")


def adminprofile(request):
    if(request.user.is_authenticated):
        user = request.user
        if(user.is_superuser):
            homes = RentHome.objects.all()
            request.homes  = homes
            users = User.objects.all()
            # request.users = users
            context = {}
            h_count = len(homes)
            u_count = len(users)
            context['users'] = users
            context['h_count'] = h_count
            context['u_count'] = u_count
            context['homes'] = homes
            return render(request, 'adminpanel.html', context)
        else:
            return redirect("/")
    else:
        return redirect("/")