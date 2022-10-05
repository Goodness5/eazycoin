from django.contrib import admin

from accounts.models import profile
from .models import PaymentProve

# Register your models here.
admin.site.register(PaymentProve)
# admin.site.register(profile)


