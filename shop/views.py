from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# # Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'shop-grid.html'
    context_object_name = 'product'
    paginate_by = 12

    def get_queryset(self):
        return self.model.objects.all().order_by('-created_at')

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