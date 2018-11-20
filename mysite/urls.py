from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from blog.views import random_post

urlpatterns = [
    path('admin-soulwawa-starbear85/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include("blog.urls", namespace='blog')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    # favicon
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('image/favicon.png'))),

    # attacker redirect
    re_path(r'^wp-content/', random_post, name='random_post'),
    re_path(r'^assets/', random_post, name='random_post'),
    re_path(r'^jm-ajax/upload_file', random_post, name='random_post'),
    re_path(r'^.*\.php/$', random_post, name='random_post'),
    path('css/', random_post, name='random_post'),
    path('js/', random_post, name='random_post'),
    path('user/', random_post, name='random_post'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]