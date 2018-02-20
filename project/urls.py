"""
ROOT URL Configuration
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('dj-admin/doc/', include('django.contrib.admindocs.urls')),
    path('dj-admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
