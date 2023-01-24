from .views import home, contact
from django.urls import path
# import views

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
]