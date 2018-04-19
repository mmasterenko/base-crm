"""
ROOT URL Configuration
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include

urlpatterns = [
    path('api/i/', include('api_urls.internal')),
    path('dj-admin/doc/', include('django.contrib.admindocs.urls')),
    path('dj-admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view
    from rest_framework.documentation import include_docs_urls
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Swagger UI 3.0 | ReDoc",
            default_version='v1',
            description="Test description",
            # terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="mmasterenko@gmail.com"),
            # license=openapi.License(name="BSD License"),
        ),
        validators=['flex', 'ssv'],
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('swagger-old', get_swagger_view(title='Swagger UI 2')),
        path('docs/', include_docs_urls(title='Built-in API',
                                        authentication_classes=[],
                                        permission_classes=[])),

        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None),
                name='schema-json'),
        path('swagger', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
        path('redoc', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
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
