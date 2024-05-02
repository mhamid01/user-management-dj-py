from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    business_name = models.CharField(max_length=255, default='')
    mailing_address = models.CharField(max_length=255, default='')
    contact_name = models.CharField(max_length=255, default='')
    contact_title = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=20, default='')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'custom_user'
