from django.shortcuts import render
# from django.db.models import Q
from .models import Product, Category
from django.views.generic import ListView
from decimal import Decimal


# # Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'shop-grid.html'
    context_object_name = 'product'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.GET.get('product_name')
        category_name = self.kwargs.get('category_name')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        if product_name:
            queryset = queryset.filter(title__icontains=product_name)
        if min_price and max_price:
            min_price_decimal = Decimal(min_price.replace('$', ''))
            max_price_decimal = Decimal(max_price.replace('$', ''))
            queryset = queryset.filter(price__gte=min_price_decimal, price__lte=max_price_decimal)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context



def sale(request):
    sale = Product.objects.filter(discount_percentage__gt=0.0)
    context = {
        'sale': sale
    }
    return render(request, 'shop-grid.html', context)

def shop_details(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'shop-details.html', context)

def shoping_cart(request):
    context = {
        'shoping_cart': shoping_cart
    }
    return render(request, 'shoping-cart.html', context)



