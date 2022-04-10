from django.urls import path
from . import views, views2

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('register_user', views.register_user, name='user_register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('house_list', views.house_list, name='house_list'),
    # path('userprofile', views2.userprofile, name='user_profile'),
    path('view_renthome', views.view_renthome, name='view_renthome'),
    # path('view_singlehome', views.view_singlehome, name='view_singlehome'),
    path('contract', views.contract, name='contract'),
    path('view_home/<int:hid>', views.view_home, name='view_home1'),
    path('view_house/<int:hid>', views.view_home, name='view_home'),
]
