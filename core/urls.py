from .views import index, contact, checkout, aboutus, subscribe
from django.urls import path
# import views

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('checkout', checkout, name='checkout'),
    path('aboutus', aboutus, name='aboutus'),
    path('subscribe', subscribe, name='subscribe'),
]