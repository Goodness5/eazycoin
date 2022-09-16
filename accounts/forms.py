from cProfile import label
from dataclasses import fields
from email.policy import default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import profile


class signup(forms.ModelForm):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput, required=True)
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1', 'first_name', 'last_name']
 
 
class signin(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        

class ProfileUpdate(forms.ModelForm):
    # username=forms.CharField(max_length=255)
    # phone = forms.CharField(max_length=20, required=True)
    # img = forms.ImageField(allow_empty_file=False)
    # dateofbirth = forms.DateField(required=True)
    class Meta:
        model = profile
        fields = ['username', 'phone', 'img', 'dateofbirth']

    
    
# '''ModelForm allows users to update their info to the database'''
# #Update email and username
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']