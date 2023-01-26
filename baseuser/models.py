from django.db import models
# from core.models import AbstractModel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/', blank=True)