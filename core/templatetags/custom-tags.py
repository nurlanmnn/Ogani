
from django.template import Library
from core.models import Advertisement, FeaturedProduct, LatestProduct


register = Library()

@register.simple_tag
def get_advertisement_all():
    return Advertisement.objects.all()

@register.simple_tag
def get_FeaturedProduct_all(limit,offset):
    return FeaturedProduct.objects.all()[limit:offset]

@register.simple_tag
def get_LatestProduct_all():
    return LatestProduct.objects.all()