from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin-soulwawa/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include("blog.urls", namespace='blog')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]