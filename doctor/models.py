from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog


class Address(models.Model):
    line1=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6)

    def __str__(self):
        return f'{self.line1} \n {self.city} \n {self.state} \n {self.pincode}'


class UserCreation(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    choice=models.CharField(max_length=30)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    pic=models.ImageField(upload_to='uploads')
    cal_id=models.CharField(max_length=200, default='')

    def __str__(self):
        return f'{self.user.username} {self.choice}'


class Speciality(models.Model):
    spec=models.CharField(max_length=50)