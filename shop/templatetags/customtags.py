from django.template import Library
from shop.models import Product, Category

register = Library()

@register.simple_tag
def get_Product_all(limit,offset):
    return Product.objects.all()[limit:offset]

@register.simple_tag
def get_Category_all():
    return Category.objects.all()