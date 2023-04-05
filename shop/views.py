from django.shortcuts import render, redirect
# from django.db.models import Q
from .models import Cart, Product, Category, CartItem
from django.views.generic import ListView
from decimal import Decimal
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html

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


def shop_details(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'shop-details.html', context)

def shoping_cart(request, total=0, quantity=0, cart_items=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            if cart_item.product.discounted_price == cart_item.product.price:
                total += (cart_item.product.price * cart_item.quantity)
            else:
                total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectNotExist:
        pass

    if not cart_items:
        message = "There is no item in your cart."
    else:
        message = ""

    context = {
        'total': total,
        # 'subtotal': subtotal,
        'quantity': quantity,
        'cart_items': cart_items,
        'message': message,
        'shoping_cart': shoping_cart
    }
    return render(request, 'shoping-cart.html', context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get cart_id with session key
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, format_html("{} was added to your cart. You can go to your cart with the link <a href='{}'>here</a>.", product.title, reverse('shopingcart')), extra_tags='safe')
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
        messages.success(request, format_html("{} was added to your cart. You can go to your cart with the link <a href='{}'>here</a>.", product.title, reverse('shopingcart')), extra_tags='safe')

    return redirect('shop')  

# remove the selected items
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('shopingcart')

# remove all
def cart_clear(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for cart_item in cart_items:
        cart_item.delete()
    return redirect('shopingcart')

# remove_from_cart
def remove_quantity(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shopingcart')

# add quantity
def add_quantity(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shopingcart')

# *********************************************************************************
# *********************************************************************************

# Here starts the wishlist

# wishlist view
def wishlistt(request):
    context = {
        'wishlistt': wishlistt
    }
    return render(request, 'wishlistt.html', context)

