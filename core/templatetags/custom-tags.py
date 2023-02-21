
from django.template import Library
from core.models import Advertisement, FeaturedProduct


register = Library()

@register.simple_tag
def get_advertisement_all():
    return Advertisement.objects.all()

@register.simple_tag
def get_FeaturedProduct_all(limit,offset):
    return FeaturedProduct.objects.all()[limit:offset]
