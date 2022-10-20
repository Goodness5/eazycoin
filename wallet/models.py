from email.policy import default
from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.forms import DateTimeField
import datetime
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class PaymentProve(models.Model):
    
    username = models.CharField(max_length=50)
    amount = models.IntegerField()
    image = models.ImageField(default='img')
    date_posted = models.DateTimeField(auto_now_add=datetime.datetime.now())
    checked = models.BooleanField(default=False) 

    def save(self):
        super().save()
        return PaymentProve
    def __str__(self):
        return f'{self.username} paymentprove'
    
    # def img(self):
    #     image = Image.image
    #     return image
        