"""
ROOT URL Configuration
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('internal-api/', include('project.internal_api_urls')),
    path('dj-admin/doc/', include('django.contrib.admindocs.urls')),
    path('dj-admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

"""
example:

/internal-api/money-flow
/internal-api/income-n-expense?depth=0&fields=one,two,three,_all_

(`-` as separator, `depth` and `fields` support, `_all_` feature)


example for future public api:

/api/v1/money-flow
/api/v1/income-n-expense
"""
