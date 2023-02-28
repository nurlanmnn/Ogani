from django.urls import path

from .views import (
    BlogAPIView,
    BlogDetailAPIView,
    NewsAPIView,
    ProductAPIView,
    ProductDetailAPIView,
    SubscriberAPIView
    )

urlpatterns = [
    path('blogs/', BlogAPIView.as_view(), name='blog'),
    path('news/', NewsAPIView.as_view(), name='news'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product'),
    path('blogs/<int:id>/', BlogDetailAPIView.as_view(), name='blog_details'),
    path('subscriber/', SubscriberAPIView.as_view(), name='subscriber'),
]