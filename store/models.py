from django.contrib.auth.models import AbstractUser
from django.db import models

class Costumer(AbstractUser):
   telephone = models.CharField(max_length=30)
   street = models.CharField(max_length=30)
   city = models.CharField(max_length=30)
   district = models.CharField(max_length=30)
   zipcode = models.CharField(max_length=30)
   country = models.CharField(max_length=30)