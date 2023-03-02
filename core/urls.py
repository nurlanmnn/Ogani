from .views import deliveryinfo, faq, index, contact, checkout, aboutus, ourservices, privacypolicy, secureshopping, subscribe
from django.urls import path
# import views

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('checkout', checkout, name='checkout'),
    path('aboutus', aboutus, name='aboutus'),
    path('subscribe', subscribe, name='subscribe'),
    path('secureshopping', secureshopping, name='secureshopping'),
    path('deliveryinfo', deliveryinfo, name='deliveryinfo'),
    path('ourservices', ourservices, name='ourservices'),
    path('privacypolicy', privacypolicy, name='privacypolicy'),
    path('faq', faq, name='faq'),
]