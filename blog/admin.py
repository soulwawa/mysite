from django.contrib import admin
from django.db import models
from .models import Post, Tag
from martor.widgets import AdminMartorWidget


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminMartorWidget
        }
    }

@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    pass
