from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.forms import DateTimeField
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class PaymentProve(models.Model):
    
    username = models.CharField(max_length=50)
    amount = models.IntegerField()
    image = models.ImageField(default = 'img', )
    date_posted = models.DateTimeField(default = timezone.now)
    
    def save(self):
        super().save(self)
    def __str__(self):
        return f'{self.username} paymentprove'
        