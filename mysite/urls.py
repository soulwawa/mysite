from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin-soulwawa/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include("blog.urls", namespace='blog'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]