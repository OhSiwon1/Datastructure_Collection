from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    number = models.CharField(max_length=20)
    profile = models.ImageField(null=True, default="profile/person.svg",upload_to="profile/")
