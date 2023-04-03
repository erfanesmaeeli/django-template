""" core URL Configuration """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts Urls 
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    
    # Main Urls
    path('', include('main.urls', namespace='main')),
    
    # Demo Urls
    path('demo/', include('demo.urls', namespace='demo')),
]
