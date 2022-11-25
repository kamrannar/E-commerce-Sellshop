from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import urls as core_urls 
from blog import urls as blog_urls
from order import urls as order_urls
from product import urls as product_urls
from accounts import urls as account_urls
from django.utils.translation import gettext_lazy as _
from product.api import urls as product
from accounts.api import urls as accounts
from blog.api import urls as blogs
from product.views import call_heavy_process


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_(''), include(core_urls)),
    path(_(''), include(blog_urls)),
    path(_(''), include(product_urls)),
    path(_(''), include(order_urls)),
    path('accounts/', include(account_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('call_heavy_process', call_heavy_process, name='call_heavy_process'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('rosetta/', include('rosetta.urls')),  

)
urlpatterns += [path('api/', include(product)),
                path('api/', include(accounts)),
                path('api/', include(blogs)),
            
                ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
