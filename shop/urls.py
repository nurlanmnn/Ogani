# from .views import shop
from django.urls import path
from .views import ProductListView, add_quantity, add_to_cart, cart_clear, remove_from_cart, remove_quantity, shop_details, shoping_cart, wishlistt

urlpatterns = [
    path('', ProductListView.as_view(), name='shop'),
    path('<slug:slug>/', shop_details, name='shopdetails'),
    path('shopingcart', shoping_cart, name='shopingcart'),
    path('categories/all', ProductListView.as_view(), name='all_categories'),
    path('categories/<str:category_name>/', ProductListView.as_view(), name='categories'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart_clear', cart_clear, name='cart_clear'),
    path('remove_quantity/<int:product_id>/', remove_quantity, name='remove_quantity'),
    path('add_quantity/<int:product_id>/', add_quantity, name='add_quantity'),
    path('wishlistt', wishlistt, name='wishlistt'),
]