from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import signup
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#registration view function
# def index(request):
#     template = loader.get_templates('signup.html')
#     return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password != password1:
            messages.danger(request, 'password does not match')
            return render(request, 'accounts/signup.html')
        user_count = User.objects.filter(email = email).count()

        if user_count > 0:
            messages.info(request,'email already exists')
            return render(request, 'accounts/signup.html')
        else:
            user = User.objects.create_user(email = email, username = username, password = password, first_name = first_name, last_name = last_name)
            messages.success(request, 'account successfully created')
            auth_user = authenticate(username = username, password = password )
            return redirect('signin')
    else:
        return render(request, 'accounts/signup.html')
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(username = username, password = password)            
        if auth_user is not None:
            login(request, auth_user)
            return redirect('dashboard')
        else:
            messages.warning(request, " you don't have an account")
            return redirect('signin')
    else:
        
        return render(request, 'accounts/signin.html')
# #registration view function
# def signin(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account Succesfully created for {username}!')

#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signin.html',{'form':form})

@login_required 
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
    
# def mywallet(request):
#     return render(request, 'accounts/mywallet.html')
        
    
