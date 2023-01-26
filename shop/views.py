from django.shortcuts import render
from .models import Shop
# # Create your views here.

def shop(request):
    shop = Shop.objects.first()
    context = {
        'shop': shop
    }
    return render(request, 'shop-grid.html', context)