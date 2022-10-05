from email import message
import mailbox
from re import X
from accounts.models import profile
from eazycoin import settings
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from .forms import PaymentForm
from django.contrib import admin
from .models import PaymentProve
from django.core.mail import send_mail, mail_admins



@login_required   
def mywallet(request):
    prof = profile.objects.all()
    context = {
    'profile': prof
  }
    # user = request.Profile
    if request.method == 'POST':
        p_form =PaymentForm(request.POST)
        if p_form.is_valid():
            obj = p_form.save(commit=False)
            obj.save()
            messages.success(request, 'your payment prove has been submitted successfully')
            mail_admins(
                'A new paymentprove has been submitted by {user.username}',
                'you received a new application. Please check it out in the administration console details are as follows',
                'from {user.email}',
            )
        else:
            messages.info(request, 'not submitted')
        
    else:
        p_form = PaymentForm()    

    return render(request, 'wallet/mywallet.html', context)

    
def services(request):
        return render(request, 'wallet/services.html')
    
    
def withdraw(request):
    return render(request, 'wallet/withdraw.html')
    

    
    