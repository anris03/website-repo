from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    catg=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.catg}'


class Blog(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='uploads')
    summary=models.CharField(max_length=300)
    content=models.TextField(default='')
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Draft(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='uploads',null=True)
    summary=models.CharField(max_length=300,null=True)
    content=models.TextField(default='')
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
