from django.db.models.signals import post_save #post_save signal is fired after an object is saved to the db
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import paymentprove

@receiver(post_save, sender = User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        #create a profile object
        paymentprove.objects.create(user = instance)

#save profile function
@receiver(post_save, sender = User)
def save_paymentprove(sender, instance, **kwargs):
    instance.paymentprove.save()
    
