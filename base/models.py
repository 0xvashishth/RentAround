from django.db import models
from django.contrib.auth.models import User


# class temp(models.Model):

class UsersData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics/')
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=200, null=True)


class RentHome(models.Model):
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    rent = models.FloatField()
    location = models.CharField(max_length=300)
    is_available = models.BooleanField()


class Images(models.Model):
    name = models.ForeignKey(RentHome, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')


class Transactions(models.Model):
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)  # User id
    hid = models.ForeignKey(RentHome, on_delete=models.CASCADE)  # House id
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()


class Contract(models.Model):
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)  # User id
    hid = models.ForeignKey(RentHome, on_delete=models.CASCADE)  # House id
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField()
    # Active, Pending, Completed, Cancelled
    status = models.CharField(max_length=100)
