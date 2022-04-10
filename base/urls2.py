from django.urls import path
from . import views,views2,views3

urlpatterns = [
    path('userprofile', views2.userprofile, name='user_profile'),
    path('useredit/', views2.useredit, name='user_profile_edit'),
    path('userdelete/', views2.userdelete, name='user_delete'),
    path('addhome', views3.addhome, name='addHome'),
    path('adminprofile', views3.adminprofile, name='adminProfile'),
]
