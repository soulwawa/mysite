from django.contrib import admin
from django.db.models import TextField
from pagedown.widgets import AdminPagedownWidget
from .models import Post, Tag

my_models = [Post, Tag]


class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {TextField: {
        'widget': AdminPagedownWidget
    }}


admin.site.register(Post, AlbumAdmin)

