from django.shortcuts import render
from .models import Product
# # Create your views here.

def shop(request):
    shop = Product.objects.first()
    context = {
        'shop': shop
    }
    return render(request, 'shop-grid.html', context)

def shop_details(request):
    context = {
        'shop_details': shop_details
    }
    return render(request, 'shop-details.html', context)

def shoping_cart(request):
    context = {
        'shoping_cart': shoping_cart
    }
    return render(request, 'shoping-cart.html', context)