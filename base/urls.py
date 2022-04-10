from django.urls import path
from . import views,views2

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('register_user', views.register_user, name='user_register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userprofile', views2.userprofile, name='user_profile'),
]
