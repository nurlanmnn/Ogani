from rest_framework import serializers
from blog.models import Blog, News, BlogCategory
from shop.models import Product, Category as Category2
from core.models import Subscriber
from baseuser.models import MyUser
from django.urls import reverse



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
        )


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'author',
            'category',
            'slug',
            'url',
        )
    
    def get_url(self, obj):
        return reverse('blog_details', kwargs={'slug': obj.slug})


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = (
            'title',
            'description',
            'image',
            'author',
        )


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = (
            'id',
            'name',
        )



class ProductSerializer(serializers.ModelSerializer):
    category = Category2Serializer()
    # url = serializers.SerializerMethodField() 

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'image',
            'image2',
            'image3',
            'image4',
            'slug',
            'category',
            'price',
            'discounted_price',
            'discount_percentage',
        )
        extra_kwargs = {
            'image2': {'required': False},
            'image3': {'required': False},
            'image4': {'required': False},
        }


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )