from django.contrib import admin
from .models import Blog, News, BlogCategory
# Register your models here.

admin.site.register(Blog)
admin.site.register(News)
admin.site.register(BlogCategory)

