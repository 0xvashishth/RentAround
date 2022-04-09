from django.urls import path
from . import views

urlpatterns = [
    # path('get_name', views.get_name, name='get_name'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register_user_page, name='userregister'),
    path('register_user', views.register_user, name='user_register')
]
