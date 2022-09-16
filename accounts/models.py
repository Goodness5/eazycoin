from distutils.command.upload import upload
import email
from email.policy import default
from time import timezone
from typing_extensions import Required, Self
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date, datetime

# # Create your models here.
# class signup(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     password1 = models.CharField(max_length=255)
class profile(models.Model):
        
    # fullname= models.CharField(max_length=255)
    username= models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    dateofbirth = models.DateField(default=date.today)
    img = models.ImageField(default= 'img')
    wallet_balance = models.CharField(max_length=20)
     
    def balance(wallet_balance):
        x = wallet_balance
        if x != 0:
            x +=0.2
            for i in x:
                i.object.filter(datetime > 5).count
                return i+1
            return x

        
    
    def save(self):
        super().save()
    def __str__(self):
        return f"{self.username} 's  profile"
  
                
                
            
            
        
    
    
    
    # def __init__(self):           
    #     img = Image.open(self.image.path)

    # #re-adjusting the size of the user profile image; to save space.
    #     if img.height > 500 and img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
        #return profile
   