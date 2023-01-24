from django.urls import path
import views


urlpatterns = [
    path('shop/', views.shop, name='shop-details'),
]