from django.urls import path

from accounts.models import profile
import eazycoin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    #path('signin/', auth_views.LoginView.as_view(template_name = 'accounts/signin.html'), name = 'signin'),
    path('signin/', views.signin, name = 'signin'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('dashboard/updateprofile/', views.profile, name= 'profile'),
    path('contact/', views.contact, name='contact'),
    path("about/", views.about, name="about"),

] 