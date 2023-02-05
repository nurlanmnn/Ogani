# from .views import shop
from django.urls import path
from .views import shop, shop_details, shoping_cart

urlpatterns = [
    path('shop', shop, name='shop'),
    path('shopdetails', shop_details, name='shopdetails'),
    path('shopingcart', shoping_cart, name='shopingcart'),
]

