from django.db import models
from decimal import Decimal
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("Category")
    
    def get_absolute_url(self):
        return reverse('categories', args=[self.name])


class Product(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/shopp')
    image2 = models.ImageField(upload_to='media/shopp2', null=True, blank=True)
    image3 = models.ImageField(upload_to='media/shopp3', null=True, blank=True)
    image4 = models.ImageField(upload_to='media/shopp4', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField(default=0.0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        discount = Decimal(str(self.discount_percentage / 100))
        self.discounted_price = self.price - (self.price * discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shopdetails', kwargs={'slug': self.slug})






