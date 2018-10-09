from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    name_url = models.CharField(max_length=50, default='<i class="fas fa-sticky-note"></i>')

    def __str__(self):
        return self.name


class Post(models.Model):
    idx = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=100)
    contents = MartorField()
    views = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField(Tag, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title



