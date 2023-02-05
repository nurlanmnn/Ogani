
from django.shortcuts import render
from .models import Blog, News
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.

def blog(request):
    blog = Blog.objects.first()
    news = News.objects.first()
    context = {
        'blog': blog,
        'news': news,
    }
    return render(request, 'blog.html', context)

def blog_details(request):
    news = News.objects.first()
    context = {
        'blog_details': blog_details,
        'news': news,
    }
    return render(request, 'blog-details.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-created_at')

