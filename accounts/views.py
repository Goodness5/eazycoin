from multiprocessing import context
# from cgitb import html
from multiprocessing import AuthenticationError
# from xml.sax.handler import feature_external_ges
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .forms import ProfileUpdate
from .models import profile
from django.contrib.auth import logout


#REGISTRATION VIEW FUNCTION
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password != password1:
            messages.warning(request, 'password does not match')
            return password
        user_count = User.objects.filter(email = email).count()

        if user_count > 0:
            messages.warning(request,'email already exists')
            return redirect('signup')
        if username == None:
            messages.warning(request, 'username feild cannot be blank')
            return username
        else:
            user = User.objects.create_user(email = email, username = username, password = password, first_name = first_name, last_name = last_name)
            user.save()
            messages.success(request, 'account successfully created')
            auth_user = authenticate(username = username, password = password )
            def mail(request):
                send_mail('welcome message', 
                      'welcome test',
                      ['settings.EMAIL_HOST_USER'],
                      ['User.email'], 
                      fail_silently=False,
                    )
                return mail(send_mail())

            return redirect('signin')
    else:
        return render(request, 'accounts/signup.html')
    
#LOGIN VIEW FUNCTION    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(username = username, password = password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('dashboard')
        else:
            messages.warning(request, "incorrect username or password")
            return redirect('signin')
    else:
        
        return render(request, 'accounts/signin.html')
    

#PROFILE VIEW DASHBOARD

@login_required    
def profile(request):
#     prof = profile.objects.all()
#     context = {
#     'profile': prof
#   }
    if request.method == 'POST': 
        username = request.POST.get('username')
        phone = request.POST['phone']
        dateofbirth = request.POST.get('date')
        img = request.POST.get('img')
        form = ProfileUpdate(request.POST)
        if form.is_valid(): 
            check = profile.username.count()
            if check == 0:
                obj = form.save(commit=False)
                obj.save()
                messages.success(request, 'success')
                return redirect('dashboard') 
            else:
                 obj = form.update()  
        else:
            messages.error(request, 'failed')
            return redirect('profile')
        
    else:
        form = ProfileUpdate()
        return render(request, 'accounts/updateprofile.html')
    
    
    
        
def contact(request):
    return render(request, 'accounts/contact.html')



def about(request):
    return render(request, 'accounts/about.html')
    
        
@login_required 
def dashboard(request):
    prof = User.objects.all()
    context = {
    'prof': profile
  }
    if User is not None:
        return render(request, 'accounts/dashboard.html', context)
    else:
        AuthenticationError('login is reqired')
        
@login_required
def logout(request):
    if User is not None:
        return redirect('index')
    else:
        AuthenticationError('you are currently not logged in')
        return redirect('signin')
    