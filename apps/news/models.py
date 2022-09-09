from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField, PPOIField

from django.db import models
from django.dispatch import receiver
from datetime import datetime

from news_app.libs.image import warm
from apps.author.models import Author


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    slug = models.SlugField(max_length=256, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='news')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news')
    published_at = models.DateTimeField(default=datetime.now)
    excerpt = models.TextField(blank=True, null=True)
    content = RichTextField()
    header_image = VersatileImageField(upload_to='news_headers/', blank=True, null=True, ppoi_field='ppoi')
    tags = models.ManyToManyField(Tag, blank=True, related_name='news')
    ppoi = PPOIField('Primary Point of Interest')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    SIZES = {
        'header_image': {
            'small': 'thumbnail__320x180',
            'medium': 'thumbnail__640x360',
        }
    }

    class Meta:
        ordering = ['-published_at']
        verbose_name_plural = 'News'

    def __str__(self) -> str:
        return self.title


@receiver(models.signals.post_save, sender=News)
def warm_images(sender, instance, **kwargs):
    warm(instance)