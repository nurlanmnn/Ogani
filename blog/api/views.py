
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import status 
from .serializers import BlogSerializer, NewsSerializer, ProductSerializer, SubscriberSerializer
from blog.models import Blog, News
from shop.models import Product
from core.models import Subscriber


class BlogAPIView(APIView):

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True, context={'request': request})
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
     
        # data = []
        # for blog in blog:
        #     data.append({
        #         'title': blog.title,
        #         'description': blog.description,
        #         # 'author' : blog.author,
        #     })
        # return Response(data=data)


class BlogDetailAPIView(APIView):

    def get(self, request, id, *args, **kwargs):
        try:
            post = Blog.objects.get(id=id)
            serializer = BlogSerializer(post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            blog = Blog.objects.get(id=kwargs['id'])
            serializer = BlogSerializer(data=request.data, instance=blog, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            blog = Blog.objects.get(id=id)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
                return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class NewsAPIView(APIView):

    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def create_product(request):
        if request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                # Only create a new Product instance if at least one image is provided
                if 'image2' in request.FILES or 'image3' in request.FILES or 'image4' in request.FILES:
                    serializer.save()
                else:
                    serializer.save(image2=None, image3=None, image4=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle GET request to display form for creating a new product
        ...



class ProductDetailAPIView(APIView):

    def get(self, request, id, *args, **kwargs):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['id'])
            serializer = ProductSerializer(data=request.data, instance=product, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
                return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class SubscriberAPIView(APIView):

    def get(self, request, *args, **kwargs):
        sub = Subscriber.objects.all()
        serializer = SubscriberSerializer(sub, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)