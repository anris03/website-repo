from unicodedata import name
from django import forms
# from .models import UserCreation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserMainF(UserCreationForm):
    CHOICES=[('1','Doctor'),('2','Patient')]
    choice=forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    line1=forms.CharField(max_length=10,label='Address Line 1')
    city=forms.CharField(max_length=100)
    state=forms.CharField(max_length=100)
    pincode=forms.CharField(max_length=100)
    pic=forms.ImageField()
    class Meta:
        model=User
        # fields='__all__'
        exclude=['groups','is_superuser','user_permissions',
                'is_staff','is_active','date_joined','last_login','password']
        



    