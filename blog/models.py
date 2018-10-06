from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


class Post(models.Model):
    idx = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=100)
    contents = MarkdownxField()
    views = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField('TAG', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
