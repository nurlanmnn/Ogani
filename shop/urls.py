# from .views import shop
from django.urls import path
from .views import ProductListView, shop_details, shoping_cart

urlpatterns = [
    path('/', ProductListView.as_view(), name='shop'),
    path('/<slug:slug>/', shop_details, name='shopdetails'),
    path('/shopingcart/', shoping_cart, name='shopingcart'),
]

