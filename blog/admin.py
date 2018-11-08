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
    exclude = ('views', )
    list_display = ['title', 'short_contents', 'get_tag_set', 'created_at', 'is_published']
    list_per_page = 10

    def short_contents(self, item):
        return item.contents[:20]

    def get_tag_set(self, item):
        return "\n".join([p.name for p in item.tag_set.all()])

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
