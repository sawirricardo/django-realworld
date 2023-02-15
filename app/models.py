from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TitleSlugDescriptionModel
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)


class User(AbstractUser):
    first_name = None
    last_name = None
    bio = models.TextField(blank=True)
    image = models.TextField(blank=True)
    followers = models.ManyToManyField("self", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name")
    created_at = CreationDateTimeField()
    updated_at = ModificationDateTimeField()


class Article(TitleSlugDescriptionModel, models.Model):
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    favoriters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="favorite_articles"
    )
    created_at = CreationDateTimeField()
    updated_at = ModificationDateTimeField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = CreationDateTimeField()
    updated_at = ModificationDateTimeField()
