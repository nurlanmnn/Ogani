from django.template import Library
from blog.models import Blog, News

register = Library()

@register.simple_tag
def get_Blog_all(limit,offset):
    return Blog.objects.all()[limit:offset]

@register.simple_tag
def get_News_all(limit,offset):
    return News.objects.all()[limit:offset]