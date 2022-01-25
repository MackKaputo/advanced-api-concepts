from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email= models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None  #required for Abstract user but we're overwriting

    #instead of username and password, we want to log in with email and passwd
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

