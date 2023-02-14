from rest_framework import serializers
from blog.models import Blog, News
from shop.models import Product


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'author',
            'slug',
        )


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = (
            'title',
            'description',
            'image',
            'author',
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'image',
            'slug',
            'category',
            'price',
            'discounted_price',
            'discount_percentage',
        )