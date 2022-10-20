
import os
import time
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.utils import timezone
...
class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
