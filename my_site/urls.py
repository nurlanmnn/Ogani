"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from core.views import index
# from django
# from core import views
# from django.conf import settings
# from django.conf.urls.static import static
# from shop import views


from core.views import *
from django.contrib import admin
from django.urls import path
# from core import views
# from blog import views
from blog.views import *
from shop.views import *
from baseuser.views import *
from django.conf import settings
from django.conf.urls.static import static
from core.urls import urlpatterns as core_urls
from blog.urls import urlpatterns as blog_urls
from shop.urls import urlpatterns as shop_urls
from baseuser.urls import urlpatterns as base_urls

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include(core_urls)),
    path('', include(blog_urls)),
    path('', include(shop_urls)),
    path('', include(base_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

