from cProfile import label
from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from re import template
from urllib import request
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .models import PaymentProve

class PaymentForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    # amount = forms.IntegerField(required=True)
    # image = forms.ImageField(required=True)
    class Meta:
        model = PaymentProve
        fields = ['username', 'amount', 'image', 'date_posted']

# class signup(forms.ModelForm):
#     username = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     firstname = forms.CharField(max_length=255)
#     lastname = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
#     password1 = forms.CharField(max_length=255)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password1']

# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']