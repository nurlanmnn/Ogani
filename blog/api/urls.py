from django.urls import path

from .views import (
    BlogAPIView,
    NewsAPIView,
    ProductAPIView,
    ProductDetailAPIView
    )

urlpatterns = [
    path('blogs/', BlogAPIView.as_view(), name='blog'),
    path('news/', NewsAPIView.as_view(), name='news'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product'),
]