from django.urls import path
from . import views

urlpatterns = [
    path('get_name', views.get_name, name='get_name'),
]