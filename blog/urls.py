from .views import blog_details, BlogListView
from django.urls import path

# import views

urlpatterns = [
    path('<slug:slug>/', blog_details, name='blog_details'),
    path('', BlogListView.as_view(), name='blog'),
    path('categories/all', BlogListView.as_view(), name='all_categorie'),
    path('categories/<str:category_name>/', BlogListView.as_view(), name='category'),
]