from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics/')
    address = models.CharField(max_length=500)
    