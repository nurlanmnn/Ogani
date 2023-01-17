from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Setting(AbstractModel):
    logo = models.ImageField(upload_to='media/logo')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    pinterest = models.CharField(max_length=100)
    paymentitem = models.ImageField(upload_to='media/payment')

    def __str__(self):
        return "My Site Settings"




class Student(AbstractModel):
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()  
    
    def __str__(self):
        return self.first_name


class Subscriber(AbstractModel):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
    

class AboutUs(AbstractModel):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ("AboutUs")


class AboutOurShop(AbstractModel):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ("AboutOurShop")


class SecureShopping(AbstractModel):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = ("SecureShopping")

    
class PrivacyPolicy(AbstractModel):
    text = models.TextField()

    def __str__(self):
        return self.text
        
    class Meta:
        verbose_name_plural = ("PrivacyPolicy")


class WhoWeAre(AbstractModel):
    text = models.TextField()

    def __str__(self):
        return 'who we are'

    class Meta:
        verbose_name_plural = ("WhoWeAre")


class Contact(AbstractModel):
    name_and_surname = models.CharField(max_length=100)
    email_address = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name_and_surname



