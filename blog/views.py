
from django.shortcuts import render
from .models import Blog, BlogCategory, News
from django.views.generic import ListView

# from django.urls import reverse_lazy
# from django.http import JsonResponse
# from .models import Blog
# from django.core.paginator import Paginator


# Create your views here.

def news(request):
    # blog = Blog.objects.first()
    news = News.objects.first()
    context = {
        # 'blog': blog,
        'news': news,
    }
    return render(request, 'blog.html', context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'post': blog,
    }
    return render(request, 'blog-details.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'
    paginate_by = 4
    
    # def get_template_names(self):
    #     slug = Blog.objects.get(slug)
    #     if 'smartphones-2023-02-28' in self.request.GET:
    #         return ['blog-details.html']
    #     else:
    #         return ['blog.html']

    def get_queryset(self):
        queryset = super().get_queryset()
        blog_name = self.request.GET.get('blog_name')
        category_name = self.kwargs.get('category_name')
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        if blog_name:
            queryset = queryset.filter(title__icontains=blog_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['blog'] = Blog.objects.all()
        context['category'] = BlogCategory.objects.all()
        return context