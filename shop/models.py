from django.db import models
from decimal import Decimal

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Product(AbstractModel):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/shopp')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField(default=0.0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        discount = Decimal(str(self.discount_percentage / 100))
        self.discounted_price = self.price - (self.price * discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



