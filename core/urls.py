""" core URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts Urls 
    path('accounts/', include('accounts.urls', namespace='accounts')),
    
    # Main Urls
    path('', include('main.urls', namespace='main')),
    
    # Demo Urls
    path('demo/', include('demo.urls', namespace='demo')),
]


# Development
if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)