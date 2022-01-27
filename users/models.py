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

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    number_of_objectives = models.IntegerField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.name}"


