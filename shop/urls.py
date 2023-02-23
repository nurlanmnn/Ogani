# from .views import shop
from django.urls import path
from .views import ProductListView, shop_details, shoping_cart, sale

urlpatterns = [
    path('', ProductListView.as_view(), name='shop'),
    path('<slug:slug>/', shop_details, name='shopdetails'),
    path('shopingcart/', shoping_cart, name='shopingcart'),
    path('categories/all', ProductListView.as_view(), name='all_categories'),
    path('<str:category_name>/', ProductListView.as_view(), name='categories'),
    path('sale/', sale, name='sales')
]

