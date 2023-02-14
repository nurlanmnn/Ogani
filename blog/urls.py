from .views import blog_details, BlogListView
from django.urls import path

# import views

urlpatterns = [
    path('/<slug:slug>/', blog_details, name='blog_details'),
    path('/', BlogListView.as_view(), name='blog'),
]