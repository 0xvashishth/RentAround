from django.urls import path
from . import views,views2

urlpatterns = [
    path('userprofile', views2.userprofile, name='user_profile'),
]
