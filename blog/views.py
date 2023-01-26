from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog(request):
    blog = Blog.objects.first()
    context = {
        'blog': blog,
    }
    return render(request, 'blog.html', context)