from .views import blog_details, BlogListView
from django.urls import path
# import views

urlpatterns = [
    # path('blog', blog, name='blog'),
    path('blogdetails', blog_details, name='blogdetails'),
    path('blog', BlogListView.as_view(), name='blog'),
]