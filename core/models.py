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
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.name_and_surname
    
    # def save(self, *args, **kwargs):
    #     self.is_check = True
    #     super(Contact, self).save(*args, **kwargs)


class Image(AbstractModel):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/aboutus')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE)

    def __str__(self):
        return self.about_us.title


class Advertisement(AbstractModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/advertisement')

    class Meta:
        verbose_name_plural = ('Advertisement')
    
    def __str__(self):
        return self.title


class FeaturedProduct(AbstractModel):
    title = models.CharField(max_length=100)
    information = models.TextField()
    image = models.ImageField(upload_to='media/featured_product')
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = ('Featured Products')
    
    def __str__(self):
        return self.title


class LatestProduct(AbstractModel):
    title = models.CharField(max_length=100)
    information = models.TextField()
    image = models.ImageField(upload_to='media/latest_product')
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = ('Latest Products')
    
    def __str__(self):
        return self.title