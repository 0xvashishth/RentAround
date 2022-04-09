from django.urls import path
from . import views

urlpatterns = [
    # path('get_name', views.get_name, name='get_name'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('login/', views.login, name='login'),
    path('register', views.register_user_page, name='userregister'),
    path('register_user', views.register_user, name='user_register')
=======
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

>>>>>>> e9eceda188278e8f6fab73dd02fee70a8090d1bc
]
