from django.db import models
from core.models import AbstractModel
from django.contrib.auth.models import User

# Create your models here.

class MyUser(AbstractModel, User):
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
