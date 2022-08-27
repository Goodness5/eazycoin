from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from .forms import PaymentForm
from .models import PaymentProve


# Create your views here.
@login_required
def wallet(request):
    form = PaymentForm()
    if request.method == 'POST':
        form =PaymentForm(request.POST)
        form.save()
        message.success(request, 'submitted')
    else: 
        form = PaymentForm() 
        return render(request, 'mywallet.html', {'form':form})



# @login_required
# def viewpayment(request):
#     if request.user.is_superuser:
#         return render(request, 'wallet/pics')
@login_required    
def mywallet(request):
    return render(request, 'wallet/mywallet.html')


    
    