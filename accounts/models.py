import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# # Create your models here.
# class signup(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     password1 = models.CharField(max_length=255)
                
                
                
# class signin(models.Model):
#     email = models.EmailField( max_length=255)
#     password = models.CharField(max_length=255)

    #overridding the save method
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     #re-adjusting the size of the user profile image; to save space.
    #     if img.height > 500 and img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
