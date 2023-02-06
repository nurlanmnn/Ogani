from django.template import Library
from shop.models import Product

register = Library()

@register.simple_tag
def get_Product_all(limit,offset):
    return Product.objects.all()[limit:offset]