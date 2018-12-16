from django.db import models
from django.contrib.auth.models import AbstractUser


class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=100, default='value')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    post_code = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=40)



