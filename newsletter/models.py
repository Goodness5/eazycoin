import logging
import os
import time
from datetime import datetime
import django
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import select_template
from django.utils.functional import cached_property
from django.utils.translation import gettext
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
