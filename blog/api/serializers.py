from rest_framework import serializers
from blog.models import Blog, News
from shop.models import Product
from core.models import Subscriber
from baseuser.models import MyUser


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
        )


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'author',
            'slug',
        )


class GETBlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'author',
            'slug',
        )


class POSTBlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

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


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )