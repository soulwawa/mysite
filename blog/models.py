from django.db import models
from django.utils import timezone
from martor.models import MartorField
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class PostManger(models.Manager):
    # todo 배포시 테스트
    def get_queryset(self):
        if User.is_superuser:
            return super(PostManger, self).get_queryset()
        else:
            return super(PostManger, self).get_queryset().filter(is_published=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    name_url = models.CharField(max_length=50, default='fas fa-sticky-note')

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Lower('name')]


class Post(models.Model):
    idx = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=100)
    contents = MartorField()
    views = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField(Tag, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManger()

    class Meta:
        ordering = ['-updated_at']

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
