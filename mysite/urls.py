from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-soulwawa/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include("blog.urls", namespace='blog')),

]
