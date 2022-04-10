from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UsersData, Contract, Transactions, RentHome
import datetime

# Create your views here.


def index(request):
    home = RentHome.objects.all()[:3]
    return render(request, "index.html",{'home':home})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # users = UsersData.objects.get(user_id=user.id)
            auth_login(request, user)
            if(not user.is_superuser):
                userdata = UsersData.objects.filter(user_id=user.id).get()
                request.session['userdata']=userdata.id
                print(userdata.usertype)
            # if users.usertype=='customer':
            #     return redirect('/')
            # else:
            #     pass
            messages.info(request, "Logged in successfully")
            return redirect('login')
        messages.warning(request, "Username or Password incorrect")
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

        if(User.objects.filter(username=username).exists()):
            # print("exist username")
            messages.warning(request, "username is not available")
            return render(request, 'register.html')
        elif(User.objects.filter(email=email).exists()):
            messages.warning(request, "Email is already taken")
            return render(request, 'register.html')
        elif(UsersData.objects.filter(mobile=mobile).exists()):
            messages.warning(request, "Your Phone is already there")
            return render(request, 'register.html')
        elif(usertype == "notnull" or usertype is None):
            messages.info(request, "Please Select usertype")
            return render(request, 'register.html')
        # print("hello user")
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=fname, last_name=lname)
        user.save()
        user1 = UsersData(user=user, usertype=usertype, mobile=mobile,
                          address=address, city=city, state=state, country=country, image=img)
        user1.save()
        # users = UsersData.objects.get(user_id=user.id)
        auth_login(request, user)
        # if users.usertype=='customer':
        #     return redirect('/')
        # else:
        #     pass
        # messages.info(request,"Logged in successfully")
        # return redirect('login')
        # print(fname)
        return redirect('/')

    return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def view_renthome(request):
    if request.user.is_authenticated:
        homes = RentHome.objects.all()
        # if homes is not None:
        return render(request, 'HousesList.html', {'homes': homes})
    return redirect('/')


def house_list(request):
    if request.user.is_authenticated:

        homeList = RentHome.objects.all()
        # for home in homes:
        # print(home.uid.user.first_name)

        # print(homes.description)

    # homesid = RentHome.objects.values_list('uid_id', flat=True)
    # print(homesid.uid)
    # users = UsersData.objects.filter(id__in=homesid).values_list('user_id', flat=True)
    # print(users)
    # user = User.objects.filter(id__in=users).values_list('id', flat=True)
    # print(user)
        if homeList is not None:
            return render(request, 'house_list.html', {'homeList': homeList, })
    return redirect('login')


# def view_home(request, hid):
#     if request.method == 'GET':
#         if(request.user.is_authenticated):
#             houseid = request.GET.get('house_id')
#             if(RentHome.objects.filter(id=houseid)):
#                 temphouse = RentHome.objects.filter(id=houseid)
#                 house = None
#                 for h in temphouse:
#                     house = h
#                 return render(request, "view_house.html", {"house": house})
#             return redirect("/house_list")
#     return redirect("/")


def view_home(request, hid):
    home = RentHome.objects.get(id=hid)
    # for h in home:

    return render(request, 'view_house.html', {'home': home})


def contract(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            uid = request.session.get('userdata')
            hid = request.POST['homeid']
            start_date = datetime.datetime.now()
            Contract(uid=uid, hid=hid, start_date=start_date).save()
    return redirect("/")
