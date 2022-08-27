from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    #path('signin/', auth_views.LoginView.as_view(template_name = 'accounts/signin.html'), name = 'signin'),
    path('signin/', views.signin, name = 'signin'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    # path('mywallet/', views.mywallet, name= 'mywallet')

] 