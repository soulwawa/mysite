from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin-soulwawa/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include("blog.urls", namespace='blog')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)