from .views import blog
from django.urls import path
# import views

urlpatterns = [
    path('blog', blog, name='blog'),
]