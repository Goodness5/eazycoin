from argparse import Namespace
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'wallet'

urlpatterns = [
    path('', views.mywallet, name='mywallet'),
    path('services/', views.services, name= 'services'),
    path('withdraw/', views.withdraw, name='withdraw'),
    
   # path('pics/download_2.jpeg', views.viewpayment)
]
