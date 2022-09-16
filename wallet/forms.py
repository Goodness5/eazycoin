from cProfile import label
from dataclasses import field, fields
from email.policy import default
from django.shortcuts import render, redirect
from pyexpat import model
from pyexpat.errors import messages
from re import template
from urllib import request
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .models import PaymentProve

class PaymentForm(forms.ModelForm):
    # username = forms.CharField(max_length=255)
    # amount = forms.IntegerField()
    # image = forms.ImageField()
    class Meta:
        model = PaymentProve
        fields = ['username', 'amount', 'image']