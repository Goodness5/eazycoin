from . import views
from django.urls import path

urlpatterns = [
    path('subscribe/', views.subscribe, 'subscribe.html'),
    
]
