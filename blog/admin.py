from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Tag

my_models = [Post, Tag]
admin.site.register(Post, MarkdownxModelAdmin)

