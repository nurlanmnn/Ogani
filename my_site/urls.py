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

from django.contrib import admin
from django.urls import path
# translation
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
# translation
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from core.views import *
from blog.views import *
from shop.views import *
from baseuser.views import *

from core.urls import urlpatterns as core_urls
from blog.urls import urlpatterns as blog_urls
from shop.urls import urlpatterns as shop_urls
from baseuser.urls import urlpatterns as base_urls
from blog.api.urls import urlpatterns as blog_api_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(core_urls)),
    # path('blog', include(blog_urls)),
    # path('shop', include(shop_urls)),
    # path('', include(base_urls)),
    path('rosetta/', include('rosetta.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('/', set_language, name='set_language'),
    path('api/', include(blog_api_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# translation
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(core_urls)),
    path('', include(base_urls)),
    path('blog', include(blog_urls)),
    path('shop', include(shop_urls)),
)

# urlpatterns += [
#     *i18n_patterns(*urlpatterns, prefix_default_language=True),
#    # YENİ
#     path("set_language/<str:language>", set_language, name="set-language"),
# ]